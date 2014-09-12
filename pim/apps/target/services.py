# -*- coding: utf-8 -*-
import common.models as MODELS
import logging

logger = logging.getLogger('app')

def addNewTarget(addTargetForm, user):

    result_flg = False
    if isUserExist(user):
        new_target = addTarget(addTargetForm)
        if new_target:
            addTargetRegister(new_target, user)
            result_flg = True

    if result_flg:
        return 'success'
    else:
        return 'fail'


def addTarget(add_target_form):

    logger.info('登録')

    if add_target_form.is_valid():
        target = add_target_form.save()
        return target
    else:
        return None


def addTargetRegister(target, user):

    target_register = MODELS.Target_register()
    target_register.target = target
    target_register.user = user
    target_register.save()


def isUserExist(user):
    logger.info('username = ' + user.username)

    # 投げられたusernameで存在チェックを行う
    isUserExist = MODELS.User.objects.filter(username=user.username).count()
    if isUserExist == 0:
        return False
    else:
        return True

def selectAllTargetList():
    return MODELS.Target.objects.all().order_by('name_en')

def selectTargetById(id):
    target = MODELS.Target.objects.get(id=id)
    return target

def selectResponsibleTargetList(user):
    """
    ユーザが担当しているターゲットリストを返す
    """
    logger.info('selectResponsibleTargetList: ' + user.username)
    target_list = MODELS.Target.objects.filter(progress_management__responsible_by=user)
    target_list = sorted(set(target_list))
    return target_list

def selectRegisteredTargetList(user):
    """
    ユーザが登録したターゲットリストを返す
    """
    logger.info('selectRegisteredTargetList: ' + user.username)
    target_list = MODELS.Target.objects.filter(target_register__user=user)
    target_list = sorted(set(target_list))
    return target_list

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
    target_list = sorted(set(target_list))
    return target_list
