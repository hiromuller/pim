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

def selectTarget(key):
    target = MODELS.Target.objects.get(id=key)
    return target