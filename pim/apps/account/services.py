# -*- coding: utf-8 -*-
import forms as FORMS
import common.models as MODELS
import logging
logger = logging.getLogger('app')

def getUserInfo(user):
    logger.info("getUserInfo = " + user.username)
    
    user_info = MODELS.User.objects.filter(username=user.username)

    # ユーザ名をセットしたUserクラスを作成
#     user_info = MODELS.User.(username=user.username)
    # progress_managementクラスを利用してフォームを作成
    # http://docs.djangoproject.jp/en/latest/topics/forms/modelforms.html
#     new_user_form = FORMS.UserForm(post_data, instance=user)

    return user_info




