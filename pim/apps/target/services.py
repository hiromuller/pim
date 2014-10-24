# -*- coding: utf-8 -*-
import common.models as MODELS
from django.db import transaction
import logging

logger = logging.getLogger('app')

@transaction.atomic
def addNewTarget(addTargetForm, user, introducer):

    result_flg = False
    if isUserExist(user):
        new_target = addTarget(addTargetForm)
        if new_target:
            addTargetRegister(new_target, user)
        if introducer:
            if isRegisteredTarget(user, introducer) or isTeamTarget(user, introducer):
                addIntroducer(new_target, introducer)
        result_flg = True

    if result_flg:
        return 'success'
    else:
        return 'fail'


@transaction.atomic
def addTarget(add_target_form):

    logger.info('登録')

    if add_target_form.is_valid():
        target = add_target_form.save()
        return target
    else:
        return None


@transaction.atomic
def addTargetRegister(target, user):

    target_register = MODELS.Target_register()
    target_register.target = target
    target_register.user = user
    target_register.save()
    return target_register

@transaction.atomic
def addIntroducer(new_target, introducer):
    """
    紹介者を登録する
    """
    logger.info('addIntroducer')

    introduce = MODELS.Introduce()
    introduce.target = new_target
    introduce.introduced_by = introducer
    introduce.save()


@transaction.atomic
def updateTarget(target_form, id):
    """
    ターゲット更新
    return success or fail
    """
    logger.info('updateTarget')

    if target_form.is_valid():
        target = target_form.save(commit=False)
        target.id = id
        target.save()
        return 'success'

    return 'fail'


def isUserExist(user):
    logger.info('username = ' + user.username)

    # 投げられたusernameで存在チェックを行う
    isUserExist = MODELS.User.objects.filter(username=user.username).count()
    if isUserExist == 0:
        return False
    else:
        return True

def userOwnsTarget(user, target):
    """
    ユーザが対象ターゲットの担当者もしくは登録者か確認する
    return boolean
    """
    logger.info('userOwnsTarget')

    registered_flg = userRegisteredTarget(user, target)
    responsible_flg = userIsResponsibleForTarget(user, target)

    if registered_flg or responsible_flg:
        return True
    else:
        return False

def userRegisteredTarget(user, target):
    """
    ユーザが対象ターゲットの登録者か確認する
    return boolean
    """
    logger.info('userRegisteredTarget')

    if MODELS.Target_register.objects.filter(user=user, target=target):
        return True
    else:
        return False

def userIsResponsibleForTarget(user, target):
    """
    ユーザが対象ターゲットの担当者か確認する
    return boolean
    """
    logger.info('userIsResponsibleForTarget')

    if MODELS.Progress_management.objects.filter(responsible_by=user, target=target):
        return True
    else:
        return False

def selectAllTargetList():
    return MODELS.Target.objects.all().order_by('name_en')

def selectTargetById(id):
    try:
        target = MODELS.Target.objects.get(id=id)
        return target
    except:
        return None

def selectResponsibleTargetList(user):
    """
    ユーザが担当しているターゲットリストを返す
    """
    logger.info('selectResponsibleTargetList: ' + user.username)
    target_list = MODELS.Target.objects.filter(progress_management__responsible_by=user, done_flg=False).order_by('reading')
    target_list = set(target_list)
    return target_list

def selectRegisteredTargetList(user):
    """
    ユーザが登録したターゲットリストを返す
    """
    logger.info('selectRegisteredTargetList: ' + user.username)
    target_list = MODELS.Target.objects.filter(target_register__user=user, done_flg=False).order_by('reading')
    target_list = set(target_list)
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
    target_list = set(target_list)
    return target_list

def selectDoneRegisteredTargetList(user):
    """
    ユーザが登録した完了ターゲットリストを返す
    """
    logger.info('selectDoneRegisteredTargetList: ' + user.username)
    target_list = MODELS.Target.objects.filter(target_register__user=user, done_flg=True).order_by('reading')
    target_list = set(target_list)
    return target_list

def selectDoneTeamTargetList(user):
    """
    チームのユーザが登録した完了ターゲットリストを返す
    """
    logger.info('selectDoneTeamTargetList: ' + user.username)
    team_list = MODELS.Team.objects.filter(membership__user=user)
    target_list = []
    for team in team_list:
        user_list = MODELS.User.objects.filter(membership__team=team)
        for user in user_list:
            target_list.extend(selectDoneRegisteredTargetList(user))
    target_list = set(target_list)
    return target_list

def isRegisteredTarget(user, target):
    """
    ターゲットがユーザの登録ターゲットか確認する
    return boolean
    """
    logger.info('isRegisteredTarget')

    if len(MODELS.Target_register.objects.filter(user=user, target=target)) == 0:
        return False
    else:
        return True

def isTeamTarget(user, target):
    """
    ターゲットがチームターゲットか確認する
    """
    logger.info('isTeamTarget')

    target_list = selectTeamTargetList(user)
    if target in target_list:
        return True
    else:
        return False

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
