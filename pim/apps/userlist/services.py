# -*- coding: utf-8 -*-
import common.models as MODELS
import logging
from django.db.models import Q

logger = logging.getLogger('app')

def getUserList():
    """
    ユーザリストを取得する
    """
    logger.info('getUserList')

    return MODELS.User.objects.all().order_by('last_login').reverse()

def getUserProgressList(user):
    """
    ユーザの進捗一覧を取得する
    return progress_managent[]
    """
    logger.info('getUserProgressList: ' + user.username)
    progress_management_list = []

    result = MODELS.Progress_management.objects.filter(responsible_by=user.username).order_by('target', 'registered_at')
    if result:
        progress_management_list = result

    return progress_management_list

def getTeamProgressList(user):
    """
    ユーザからチームの別メンバの進捗を取得する
    return progress_management[]
    """
    logger.info('getTeamProgressList: ' + user.username)
    team_progress_lists = []

    # 自分のメンバーシップ取得
    my_membership = MODELS.Membership.objects.filter(user=user)

    # 1ユーザ1チームにしか対応していないため、とれた1件目のメンバーシップ取得
    if len(my_membership) == 1:
        my_membership = my_membership[0]

        #  チームが同一の自分以外のメンバーシップを取得
        team_membership_list = MODELS.Membership.objects.filter(team=my_membership.team).exclude(user=user)

        # 自分以外のチームのメンバーシップのユーザに紐づく進捗をリストに詰める
        for team_membership in team_membership_list:
            team_progress_list= MODELS.Progress_management.objects.filter(responsible_by=team_membership.user).order_by('target', 'registered_at')
            team_progress_lists.append(team_progress_list)

    else:
        # 自分のメンバーシップが1件以外の場合、何もしない
        pass

    return team_progress_lists

def getNumTarget(user):
    """
    ユーザが登録したターゲット数を返す
    return int
    """

    return  MODELS.Target.objects.filter(target_register__user=user).count()

def selectUserById(user_id):
    logger.info('selectUserById : ' + user_id)
    try:
        user = MODELS.User.objects.get(username=user_id)
        return user
    except MODELS.User.DoesNotExist:
        return None

def selectTeamsByUser(user):
    """
    ユーザが所属するチームのリストを返す
    """
    logger.info('selectTeamsByUser')
    team_list = []
    membership_list = MODELS.Membership.objects.filter(user=user)
    if len(membership_list) >= 1:
        for membership in membership_list:
            team_list.append(membership.team)
    return team_list

def selectRelatedTarget(user):
    """
    ユーザが登録した、もしくは担当しているターゲットを取得する
    return target[]
    """
    return MODELS.Target.objects.filter(Q(progress_management__responsible_by=user) | Q(target_register__user=user))

def selectActiveUser(target):
    """
    ターゲットの現担当者を帰す
    return user or None
    """
    try:
        if target.taken_flg:
            latest_progress_management = MODELS.Progress_management.objects.filter(target=target).latest('registered_at')
            return latest_progress_management.responsible_by
        else:
            return None
    except:
        return None

def deleteUser(user):
    """
    ユーザを削除する
    連動して削除するものは以下
    membership, invitation, progress_management, target_register、target、introducer、
    もしチーム管理者の場合、teamとそれに紐づくmembershipとinvitation全て

    もし削除対象ユーザの登録ターゲットの担当者が別ユーザである場合、ターゲットは担当者の登録ターゲットとなる

    削除順番(チーム関連)
    1.own membership or team's membership
    2.own invitation or team's invitation
    3.team if admin

    削除順番(ターゲット関連)
    1.もし登録ターゲットの担当が別ユーザだった場合、ターゲットは担当者の登録ターゲットとなる = target_registerをupdate
    2.削除対象ターゲットがintroducerのintroduceレコードを全て削除
    3.削除対象ターゲットがターゲットの全てのtarget_register
    4.削除対象がターゲットの全てのprogress_management
    5.削除対象ターゲット

    """

    #チーム関連項目削除
    team_list = selectTeamsByUser(user)

    for team in team_list:
        membership = MODELS.Membership.objects.get(user=user, team=team)
        if membership.team_admin_flg:
            MODELS.Membership.objects.filter(team = team).delete()
            MODELS.Invitation.objects.filter(team = team).delete()
            team.delete()
        else:
            membership.delete()
            MODELS.Invitation.objects.filter(invited_user=user).delete()

    #ターゲット関連項目削除
    target_list = selectRelatedTarget(user)

    for target in target_list:
        register_flg = False
        responsible_flg = False
        if MODELS.User.objects.get(target_register__target=target) == user:
            register_flg = True
        if user in MODELS.User.objects.filter(progress_management__target=target):
            responsible_flg = True

        if register_flg & responsible_flg:
            MODELS.Introduce.objects.filter(Q(target=target) | Q(introduced_by=target)).delete()
            MODELS.Progress_management.objects.filter(target=target).delete()
            MODELS.Target_register.objects.filter(target=target).delete()
            target.delete()
        elif responsible_flg:
            MODELS.Progress_management.objects.filter(target=target,responsible_by=user).delete()
        elif register_flg:
            active_user = selectActiveUser(target)
            if active_user:
                target_register = MODELS.Target_register.objects.get(target=target)
                target_register.user = active_user
                target_register.save()

                MODELS.Progress_management.objects.filter(target=target, responsible_by=user).delete()
            else:
                MODELS.Introduce.objects.filter(Q(target=target) | Q(introduced_by=target)).delete()
                MODELS.Progress_management.objects.filter(target=target).delete()
                MODELS.Target_register.objects.filter(target=target).delete()
                target.delete()

    user.is_active = False
    user.save()
    return "success"

def activateUser(user):
    """
    ユーザを再稼動させる
    return string
    """
    user.is_active = True
    user.save()

    return "success"

def deactivateUser(user):
    """
    ユーザを再稼動させる
    return string
    """
    user.is_active = False
    user.save()

    return "success"
