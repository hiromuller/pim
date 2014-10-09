# -*- coding: utf-8 -*-
# targetlist views
from django.shortcuts import render
from django.core.context_processors import csrf
import configs as CONFIG
import forms as FORMS
import services as SERVICES
import messages as MSGS
import consts as CONSTS
import logging

logger = logging.getLogger('app')

def index(request):
    """
    ターゲット一覧画面インデックス
    最初に必ず通る
    """
    logger.info('ターゲットリスト画面開始')
    forms = {'addForm':FORMS.TargetForm()}
    c = {}
    c.update(forms)
    return show(request, c)

def add(request):
    """
    ターゲット登録
    """
    logger.info('ターゲット登録')

    if request.method == 'POST':
        addTargetForm = FORMS.TargetForm(request.POST, request.FILES)
        result = SERVICES.addNewTarget(addTargetForm, request.user)

        if not result == 'success':
            fail_form = FORMS.TargetForm(request.POST)
            c = {'addForm':fail_form}
            c.update({'form_message':MSGS.ADD_FAIL})

            return show(request, c)

    c = {'form_message': MSGS.ADD_SUCCESS}
    c.update({'addForm':FORMS.TargetForm()})
    return show(request, c)

def targetUpdate(request):
    """
    ターゲット更新
    """
    logger.info('ターゲット更新')
    c = {}
    result = ''

    if request.method == 'POST':
        target_form = FORMS.TargetForm(request.POST)
        target_id = request.POST['id']
        target = SERVICES.selectTargetById(target_id)
        if SERVICES.userOwnsTarget(request.user, target):
            result = SERVICES.updateTarget(target_form, target_id)

    if result == 'success':
        c.update({'form_message': MSGS.TARGET_UPDATE_SUCCESS})
    else:
        c.update({'form_message':MSGS.TARGET_UPDATE_FAIL})

    target = SERVICES.selectTargetById(target_id)
    c.update({'target':target})

    targetForm = FORMS.TargetForm(instance=target)
    c.update({'targetForm':targetForm})
    return targetDetailShow(request, c)

def targetDetail(request):
    """
    ターゲット詳細
    """
    logger.info('ターゲット詳細表示')

    if request.method == "POST":
        key = request.POST["key"]

    if key is None:
        return index(request)

    c = {}
    target = SERVICES.selectTargetById(key)
    c.update({'target':target})

    targetForm = FORMS.TargetForm(instance=target)
    c.update({'targetForm':targetForm})

    return targetDetailShow(request, c)


def targetDetailShow(request, c):
    """
    ターゲット詳細表示
    """
    main_url = CONFIG.TOP_URL
    page_title = CONFIG.TARGET_PAGE_TITLE_URL
    main_content = CONFIG.TARGET_DETAIL
    sub_content = CONFIG.TARGET_SUB_URL

    url_dict = {'main_url':main_url,
                'page_title':page_title,
                'main_content':main_content,
                'sub_content':sub_content}
    c.update(csrf(request))
    c.update(url_dict)
    c.update(CONFIG.ACTION_DICT)
    return render(request, 'common/main.html', c)

def show(request, c):
    """
    ターゲット一覧表示メソッド
    URLなど必要な値をセットし、表示する
    """
    logger.info('ターゲットリスト表示')

#    target_list = SERVICES.selectAllTargetList()
#    c.update({'target_list':target_list})

    responsible_target_list = SERVICES.selectResponsibleTargetList(request.user)
    registered_target_list = SERVICES.selectRegisteredTargetList(request.user)
    team_target_list = SERVICES.selectTeamTargetList(request.user)

    target_list_list = []
    target_list_list.append([CONSTS.RESPONSIBLE_TARGET_LIST_NAME,
                             responsible_target_list])
    target_list_list.append([CONSTS.REGISTERED_TARGET_LIST_NAME,
                             registered_target_list])
    target_list_list.append([CONSTS.TEAM_TARGET_LIST_NAME,
                             team_target_list])
    c.update({'target_list_list':target_list_list})

    main_url = CONFIG.TOP_URL
    page_title = CONFIG.TARGET_PAGE_TITLE_URL
    main_content = CONFIG.TARGET_MAIN_URL
    sub_content = CONFIG.TARGET_SUB_URL

    url_dict = {'main_url':main_url,
                'page_title':page_title,
                'main_content':main_content,
                'sub_content':sub_content}
    c.update(csrf(request))
    c.update({'html_title':CONFIG.TARGET_HTML_TITLE})
    c.update(url_dict)
    c.update(CONFIG.ACTION_DICT)
    return render(request, 'common/main.html', c)
