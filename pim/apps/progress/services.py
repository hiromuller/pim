# -*- coding: utf-8 -*-
import forms as FORMS
import common.models as MODELS
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
    return 'success'

def getUserProgressList(user):
    return MODELS.Progress_management.objects.filter(responsible_by=user.username).order_by('target', 'registered_at')

def getTeamProgressList(user):
    """
    ユーザからチームの別メンバの進捗を取得する
    return progress_management[]
    """
    # 自分のメンバーシップ取得
    my_membership = MODELS.Membership.objects.get(user=user)

    #  チームが同一の自分以外のメンバーシップを取得
    team_membership_list = MODELS.Membership.objects.filter(team=my_membership.team.pk).exclude(user=user)

    # 自分以外のチームのメンバーシップのユーザに紐づく進捗をリストに詰める
    team_progress_lists = []
    for team_membership in team_membership_list:
        team_progress_list= MODELS.Progress_management.objects.filter(responsible_by=team_membership.user).order_by('target', 'registered_at')
        team_progress_lists.append(team_progress_list)

    return team_progress_lists



