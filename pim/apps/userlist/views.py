# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.context_processors import csrf
import configs as CONFIG
import settings as SETTING
import services as SERVICES
import messages as MSGS
import logging

logger = logging.getLogger('app')

def index(request):
    logger.info('ユーザ管理')
    c = {}

    return show(request, c)

def deleteUser(request):
    """
    ユーザを削除する
    """
    logger.info('ユーザ削除')
    c = {}
    if request.method == "POST":
        username = request.POST["object_id"]

    user = SERVICES.selectUserById(username)

    if user:
        result = SERVICES.deleteUser(user)

    if result == 'success':
        c.update({'list_form_message': MSGS.DELETE_USER_SUCCESS})
    else:
        c.update({'list_form_message':MSGS.DELETE_USER_FAIL})


    return show(request, c)

def deactivateUser(request):
    """
    ユーザをロックする
    """
    logger.info('ユーザロック')
    c = {}

    if request.method == "POST":
        username = request.POST['object_id']

    user = SERVICES.selectUserById(username)

    if user:
        result = SERVICES.deactivateUser(user)

    if result == 'success':
        c.update({'list_form_message': MSGS.DEACTIVATE_USER_SUCCESS})
    else:
        c.update({'list_form_message':MSGS.DEACTIVATE_USER_FAIL})

    return show(request, c)

def activateUser(request):
    """
    ユーザを再稼動させる
    """
    logger.info('ユーザ再稼動')
    c = {}

    if request.method == "POST":
        username = request.POST['object_id']

    user = SERVICES.selectUserById(username)

    if user:
        result = SERVICES.activateUser(user)

    if result == 'success':
        c.update({'list_form_message': MSGS.ACTIVATE_USER_SUCCESS})
    else:
        c.update({'list_form_message':MSGS.ACTIVATE_USER_FAIL})

    return show(request, c)

def show(request, c):
    userlist = SERVICES.getUserList()
    c.update({'userlist':userlist})

    num_target_dict = {}
    for user in userlist:
        num_target_dict.update({user:SERVICES.getNumTarget(user)})
    c.update({'num_target_dict':num_target_dict})
    main_url = CONFIG.TOP_URL
    page_title = CONFIG.USERLIST_PAGE_TITLE_URL
    main_content = CONFIG.USERLIST_MAIN_URL
    sub_content = CONFIG.USERLIST_SUB_URL
    action_dict = CONFIG.ACTION_DICT
#     user_dict = {'user':user}
    url_dict = {'main_url':main_url,
                'page_title':page_title,
                'main_content':main_content,
                'sub_content':sub_content,
                'insert_button':'-'
                }
    c.update({'master_user_name':SETTING.MASTER_USER_NAME})
    c.update(csrf(request))
    c.update({'html_title':CONFIG.USERLIST_HTML_TITLE})
    c.update(url_dict)
    c.update(action_dict)
#     c.update(user_dict)
    return render(request, 'common/main.html', c)