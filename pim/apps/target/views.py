# -*- coding: utf-8 -*-
# targetlist views
from django.shortcuts import render
from django.core.context_processors import csrf
import configs as CONFIG
import forms as FORMS
import services as SERVICES
import messages as MSGS
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

def target_detail(request):
    """
    ターゲット詳細
    """
    logger.info('ターゲット詳細表示')

    if request.method == "POST":
        key = request.POST["key"]
        
    if key is None:
        return index(request)

    c = {}
    target = SERVICES.selectTarget(key)
    c.update({'target':target})

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
    
    target_list = SERVICES.selectAllTargetList()
    c.update({'target_list':target_list})

    main_url = CONFIG.TOP_URL
    page_title = CONFIG.TARGET_PAGE_TITLE_URL
    main_content = CONFIG.TARGET_MAIN_URL
    sub_content = CONFIG.TARGET_SUB_URL

    url_dict = {'main_url':main_url, 
                'page_title':page_title, 
                'main_content':main_content,
                'sub_content':sub_content}
    c.update(csrf(request))
    c.update(url_dict)
    c.update(CONFIG.ACTION_DICT)
    return render(request, 'common/main.html', c)
    