# -*- coding: utf-8 -*-
import forms as FORMS
import common.models as MODELS

def addProgress(request):
    print 'addProgress'

    print 'username = ' + request.user.username
    # ユーザ名をセットしたUserクラスを作成
    user = MODELS.User(username=request.user.username)
    # responsible_byに作成したuserモデルをセットしてProgress_managementクラスを作成
    progress_management = MODELS.Progress_management(responsible_by=user)
    # progress_managementクラスを利用してフォームを作成
    # http://docs.djangoproject.jp/en/latest/topics/forms/modelforms.html
    new_progress_form = FORMS.ProgressManagementForm(request.POST, instance=progress_management)

    print new_progress_form.errors
    print new_progress_form
    if new_progress_form.is_valid():
        print 'is_valid'
        new_progress_form.save()
        return 'success'
    else:
        return 'fail'
