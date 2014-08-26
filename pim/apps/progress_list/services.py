# -*- coding: utf-8 -*-
import forms as FORMS
import common.models as MODELS
import logging

logger = logging.getLogger('app')

def addProgress(request):
    logger.info('addProgress')

    logger.info('username = ' + request.user.username)

    # 投げられたusernameで存在チェックを行う
    isUserExist = MODELS.User.objects.filter(username=request.user.username).count()
    if isUserExist == 0:
        return 'fail'

    # ユーザ名をセットしたUserクラスを作成
    user = MODELS.User(username=request.user.username)
    # responsible_byに作成したuserモデルをセットしてProgress_managementクラスを作成
    progress_management = MODELS.Progress_management(responsible_by=user)
    # progress_managementクラスを利用してフォームを作成
    # http://docs.djangoproject.jp/en/latest/topics/forms/modelforms.html
    new_progress_form = FORMS.ProgressManagementForm(request.POST, instance=progress_management)

    if new_progress_form.is_valid():
        logger.info('is_valid')
        new_progress_form.save()
        return 'success'
    else:
        return 'fail'
