# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.context_processors import csrf
import configs as CONFIG
import settings as SETTING
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
    return list_init(request, c)


def add(request):
    logger.info('add')

    if request.method == 'POST':
        result = SERVICES.addProgress(request.user, request.POST)
        if not result == 'success':
            fail_form = FORMS.ProgressManagementForm(request.user, request.POST)
            c = {'form':fail_form}
            c.update({'form_message':MSGS.ADD_FAIL})
            return list_init(request, c)
    c = {'form_message': MSGS.ADD_SUCCESS}
    c.update({'form':FORMS.ProgressManagementForm(request.user, )})
    return list_init(request, c)

def update(request):
    logger.info('update')

    if request.method == 'POST':
        result = SERVICES.updateProgress(request.user, request.POST)
        if not result == 'success':
            fail_form = FORMS.ProgressManagementForm(request.user, request.POST)
            c = {'form':fail_form}
            c.update({'form_message':MSGS.UPD_FAIL})
            return list_init(request, c)
    c = {'form_message': MSGS.UPD_SUCCESS}
    c.update({'form':FORMS.ProgressManagementForm(request.user, )})
    return list_init(request, c)

def search(request):
    logger.info('search')
    form = {'form':ProgressManagementForm(request.user)}
    c = {}
    c.update(form)

    if request.method == 'POST':
        key = request.POST['key']
        if key:
            # 担当者の進捗一覧を取得し、返却する
            user_progress_list = SERVICES.getUserProgressListByKey(request.user, key)
            c.update({'user_progress_list':user_progress_list})

            # 担当者の所属するチームの別メンバの進捗を取得し、返却する
            team_progress_lists = SERVICES.getTeamProgressList(request.user, key)
            c.update({'team_progress_lists':team_progress_lists})
            c.update({'key':key})
            return show(request, c)

    return list_init(request, c)

def list_init(request, c):
    # 担当者の進捗一覧を取得し、返却する
    user_progress_list = SERVICES.getUserProgressList(request.user)
    c.update({'user_progress_list':user_progress_list})

    # 担当者の所属するチームの別メンバの進捗を取得し、返却する
    team_progress_lists = SERVICES.getTeamProgressList(request.user)
    c.update({'team_progress_lists':team_progress_lists})

    return show(request, c)

def show(request, c):
    logger.info('show')
    main_url = CONFIG.TOP_URL
    page_title = CONFIG.PROGRESS_PAGE_TITLE_URL
    main_content = CONFIG.PROGRESS_MAIN_URL
    sub_content = CONFIG.PROGRESS_SUB_URL
    insert_button = CONFIG.INSERT_BUTTON
    search_action= CONFIG.ACTION_PROGRESS_SEARCH
#     form = {'form':ProgressManagementForm()}
    url_dict = {'main_url':main_url,
                'page_title':page_title,
                'main_content':main_content,
                'sub_content':sub_content,
                'insert_button':insert_button,
                'search_action':search_action}
    c.update({'master_user_name':SETTING.MASTER_USER_NAME})
    c.update(csrf(request))
    c.update({'html_title':CONFIG.PROGRESS_HTML_TITLE})
    c.update(url_dict)
    c.update(CONFIG.ACTION_DICT)
    return render(request, 'common/main.html', c)