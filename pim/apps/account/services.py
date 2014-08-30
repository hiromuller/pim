# -*- coding: utf-8 -*-
import common.models as MODELS
import logging
logger = logging.getLogger('app')

def getUserInfo(username):
    logger.info("getUserInfo = " + username)
    
    user_info = MODELS.User.objects.get(pk=username)

    return user_info

def updateUserInfo(user_form):
    logger.info("updateUserInfo")

    if user_form.is_valid():
        user_form.save()
        return 'success'
    else:
        return 'fail'





