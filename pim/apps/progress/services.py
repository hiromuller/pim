# -*- coding: utf-8 -*-
import forms as FORMS
import common.models as MODELS
import consts as CONSTS
import logging
logger = logging.getLogger('app')

def addProgress(user, post_data):
    logger.info('addProgress')

    logger.info('username = ' + user.username)

    # 投げられたusernameで存在チェックを行う
    isUserExist = MODELS.User.objects.filter(username=user.username).count()
    if isUserExist == 0:
        return 'fail'

    # ユーザ名をセットしたUserクラスを作成
    user = MODELS.User(username=user.username)
    # responsible_byに作成したuserモデルをセットしてProgress_managementクラスを作成
    progress_management = MODELS.Progress_management(responsible_by=user)
    progress_management.target = MODELS.Target.objects.get(id=post_data['select_target'])

    # progress_managementクラスを利用してフォームを作成
    # http://docs.djangoproject.jp/en/latest/topics/forms/modelforms.html
    new_progress_form = FORMS.ProgressManagementForm(user, post_data, instance=progress_management)

    if new_progress_form.is_valid():
        logger.info('is_valid')
        new_progress_form.save()
        updateTargetTakenFlg(post_data)
        return 'success'
    else:
        return 'fail'

def updateProgress(user, post_data):
    logger.info('updateProgress')

    logger.info('username = ' + user.username)

    # 投げられたusernameで存在チェックを行う
    isUserExist = MODELS.User.objects.filter(username=user.username).count()
    if isUserExist == 0:
        return 'fail'

    # Progress_managementクラスを作成
    progress_management = MODELS.Progress_management.objects.get(pk=post_data['user_progress_id'])
    progress_management.target = MODELS.Target.objects.get(id=post_data['select_target'])
    progress_management.relationship = post_data['relationship']
    progress_management.progress = post_data['progress']
    progress_management.remarks = post_data['remarks']
    progress_management.save()

    updateTargetTakenFlg(post_data)

    return 'success'

def updateTargetTakenFlg(post_data):
    """
    ターゲットの担当者ありフラグを進捗状況によって更新する
    """
    logger.info('updateTargetTakenFlg')
    target = MODELS.Target.objects.get(id=post_data['select_target'])
    if post_data['progress'] == CONSTS.PROGRESS_COMPLETED or post_data['progress'] == CONSTS.PROGRESS_FINISHED:
        target.taken_flg = 0
        target.save()
    else:
        if target.taken_flg == 0:
            target.taken_flg = 1
            target.save()

    return 'success'

def getUserProgressList(user):
    return MODELS.Progress_management.objects.filter(responsible_by=user.username).order_by('target', 'registered_at')

def getTeamProgressList(user):
    """
    ユーザからチームの別メンバの進捗を取得する
    return progress_management[]
    """
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

def selectTeamTargetList(user):
    """
    チームのユーザが登録したターゲットリストを返す
    """
    logger.info('selectTeamTargetList: ' + user.username)
    team_list = MODELS.Team.objects.filter(membership__user=user)
    target_list = []
    for team in team_list:
        user_list = MODELS.User.objects.filter(membership__team=team)
        for user in user_list:
            target_list.extend(selectRegisteredTargetList(user))
    target_list = set(target_list)
    return target_list

def selectRegisteredTargetList(user):
    """
    ユーザが登録したターゲットリストを返す
    """
    logger.info('selectRegisteredTargetList: ' + user.username)
    target_list = MODELS.Target.objects.filter(target_register__user=user).order_by('reading')
    target_list = set(target_list)
    return target_list

def targetTakenByOthers(target, user):
    """
    ターゲットがほかのユーザに採られているか
    return boolean
    """
    if target.taken_flg == True:
        if not user == selectLatestProgressManagementByTarget(target).responsible_by:
            return True
    return False

def selectLatestProgressManagementByTarget(target):
    """
    ターゲットをキーに最新の進捗状況を返す
    """
    return MODELS.Progress_management.objects.filter(target=target).latest('registered_at')

def hasTeam(user):
    """
    ユーザがチームに所属しているか確認する
    return boolean
    """
    logger.info('hasTeam: '  + user.username)

    if len(MODELS.Membership.objects.filter(user=user)) == 0:
        logger.info('False')
        return False
    else:
        logger.info('True')
        return True
