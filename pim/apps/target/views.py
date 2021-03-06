# -*- coding: utf-8 -*-
# targetlist views
from django.shortcuts import render
from django.core.context_processors import csrf
import configs as CONFIG
import settings as SETTING
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
    return list_init(request, c)

def add(request):
    """
    ターゲット登録
    """
    logger.info('ターゲット登録')

    if request.method == 'POST':
        addTargetForm = FORMS.TargetForm(request.POST, request.FILES)
        introducer = SERVICES.selectTargetById(request.POST['introducer'])
        result = SERVICES.addNewTarget(addTargetForm, request.user, introducer)

        if not result == 'success':
            fail_form = FORMS.TargetForm(request.POST)
            c = {'addForm':fail_form}
            c.update({'form_message':MSGS.ADD_FAIL})

            return list_init(request, c)

    c = {'form_message': MSGS.ADD_SUCCESS}
    c.update({'addForm':FORMS.TargetForm()})
    return list_init(request, c)

def targetUpdate(request):
    """
    ターゲット更新
    """
    logger.info('ターゲット更新')
    c = {}
    result = ''

    if request.method == 'POST':
        target_form = FORMS.TargetForm(request.POST, request.FILES)
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
    c.update({'master_user_name':SETTING.MASTER_USER_NAME})
    c.update({'main_only':',main_only'})
    c.update(csrf(request))
    c.update(url_dict)
    c.update(CONFIG.ACTION_DICT)
    return render(request, 'common/main.html', c)

def targetSearch(request):
    """
    ターゲット検索
    """
    logger.info('ターゲットリスト画面開始')
    forms = {'addForm':FORMS.TargetForm()}
    c = {}
    c.update(forms)

    if request.method == 'POST':
        key = request.POST["key"]
        if key:

        #表示するターゲットを取得する
            responsible_target_list = SERVICES.selectResponsibleTargetListByKey(request.user, key)
            registered_target_list = SERVICES.selectRegisteredTargetListByKey(request.user, key)
            team_target_list = SERVICES.selectTeamTargetListByKey(request.user, key)
            if SERVICES.hasTeam(request.user):
                done_target_list = SERVICES.selectDoneTeamTargetListByKey(request.user, key)
            else:
                done_target_list = SERVICES.selectDoneRegisteredTargetListByKey(request.user, key)

            target_list_list = []
            target_list_list.append([CONSTS.RESPONSIBLE_TARGET_LIST_NAME,
                                     responsible_target_list])
            target_list_list.append([CONSTS.REGISTERED_TARGET_LIST_NAME,
                                     registered_target_list])
            target_list_list.append([CONSTS.TEAM_TARGET_LIST_NAME,
                                     team_target_list])
            target_list_list.append([CONSTS.DONE_TARGET_LIST_NAME,
                                     done_target_list])
            c.update({'target_list_list':target_list_list})
            c.update({'key':key})
            return show(request, c)
    return list_init(request, c)

def list_init(request, c):
    """
    ターゲット一覧表示メソッド
    URLなど必要な値をセットし、表示する
    """
    logger.info('ターゲットリスト表示')

#    target_list = SERVICES.selectAllTargetList()
#    c.update({'target_list':target_list})

    #表示するターゲットを取得する
    responsible_target_list = SERVICES.selectResponsibleTargetList(request.user)
    registered_target_list = SERVICES.selectRegisteredTargetList(request.user)
    team_target_list = SERVICES.selectTeamTargetList(request.user)
    if SERVICES.hasTeam(request.user):
        done_target_list = SERVICES.selectDoneTeamTargetList(request.user)
    else:
        done_target_list = SERVICES.selectDoneRegisteredTargetList(request.user)

    target_list_list = []
    target_list_list.append([CONSTS.RESPONSIBLE_TARGET_LIST_NAME,
                             responsible_target_list])
    target_list_list.append([CONSTS.REGISTERED_TARGET_LIST_NAME,
                             registered_target_list])
    target_list_list.append([CONSTS.TEAM_TARGET_LIST_NAME,
                             team_target_list])
    target_list_list.append([CONSTS.DONE_TARGET_LIST_NAME,
                             done_target_list])
    c.update({'target_list_list':target_list_list})

    return show(request, c)

def show(request, c):
    #紹介者用ターゲットリストをセット
    registered_target_list = SERVICES.selectRegisteredTargetList(request.user)
    team_target_list = SERVICES.selectTeamTargetList(request.user)
    if SERVICES.hasTeam(request.user):
        introducer_form = {'introducer_form':FORMS.IntroducerForm(team_target_list)}
    else:
        introducer_form = {'introducer_form':FORMS.IntroducerForm(registered_target_list)}
    c.update(introducer_form)

    main_url = CONFIG.TOP_URL
    page_title = CONFIG.TARGET_PAGE_TITLE_URL
    main_content = CONFIG.TARGET_MAIN_URL
    sub_content = CONFIG.TARGET_SUB_URL
    insert_button = CONFIG.INSERT_BUTTON
    search_action= CONFIG.ACTION_TARGET_SEARCH

    url_dict = {'main_url':main_url,
                'page_title':page_title,
                'main_content':main_content,
                'sub_content':sub_content,
                'insert_button':insert_button,
                'search_action':search_action}
    c.update({'master_user_name':SETTING.MASTER_USER_NAME})
    c.update(csrf(request))
    c.update({'html_title':CONFIG.TARGET_HTML_TITLE})
    c.update(url_dict)
    c.update(CONFIG.ACTION_DICT)
    return render(request, 'common/main.html', c)
