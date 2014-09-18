# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.context_processors import csrf
import configs as CONFIG
from progress.forms import ProgressManagementForm
import forms as FORMS
import services as SERVICES
import messages as MSGS
import logging
logger = logging.getLogger('app')

# 
def index(request):

    logger.info('index')

    form = {'form':ProgressManagementForm(request.user)}
    c = {}    
    c.update(form)
    return show(request, c)


def add(request):
    logger.info('add')

    if request.method == 'POST':
        result = SERVICES.addProgress(request.user, request.POST)
        if not result == 'success':
            fail_form = FORMS.ProgressManagementForm(request.user, request.POST)
            c = {'form':fail_form}
            c.update({'form_message':MSGS.ADD_FAIL})
            return show(request, c)
    c = {'form_message': MSGS.ADD_SUCCESS}
    c.update({'form':FORMS.ProgressManagementForm(request.user, )})
    return show(request, c)

def update(request ):
    logger.info('update')

    if request.method == 'POST':
        result = SERVICES.updateProgress(request.user, request.POST)
        if not result == 'success':
            fail_form = FORMS.ProgressManagementForm(request.user, request.POST)
            c = {'form':fail_form}
            c.update({'form_message':MSGS.UPD_FAIL})
            return show(request, c)
    c = {'form_message': MSGS.UPD_SUCCESS}
    c.update({'form':FORMS.ProgressManagementForm(request.user, )})
    return show(request, c)

def show(request, c):

    logger.info('show')

    # 担当者の進捗一覧を取得し、返却する
    user_progress_list = SERVICES.getUserProgressList(request.user)
    c.update({'user_progress_list':user_progress_list})

    # 担当者の所属するチームの別メンバの進捗を取得し、返却する
    team_progress_lists = SERVICES.getTeamProgressList(request.user)
    c.update({'team_progress_lists':team_progress_lists})

    main_url = CONFIG.TOP_URL
    page_title = CONFIG.PROGRESS_PAGE_TITLE_URL
    main_content = CONFIG.PROGRESS_MAIN_URL
    sub_content = CONFIG.PROGRESS_SUB_URL
#     form = {'form':ProgressManagementForm()}
    url_dict = {'main_url':main_url, 
                'page_title':page_title, 
                'main_content':main_content,
                'sub_content':sub_content}
    c.update(csrf(request))
    c.update(url_dict)
    c.update(CONFIG.ACTION_DICT)
    return render(request, 'common/main.html', c)