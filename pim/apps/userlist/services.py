# -*- coding: utf-8 -*-
import common.models as MODELS
import logging

logger = logging.getLogger('app')

def getUserList():
    """
    ユーザリストを取得する
    """
    logger.info('getUserList')

    return MODELS.User.objects.all()

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