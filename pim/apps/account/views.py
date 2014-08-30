# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.context_processors import csrf
import configs as CONFIG
import services as SERVICES
import logging
import messages as MSGS
from account.forms import UserForm
logger = logging.getLogger('app')

def index(request):
    logger.info('index')

    logger.info('username = ' + request.user.username)

    user = SERVICES.getUserInfo(request.user.username)
    form = UserForm(instance=user)
    c = {'form':form}

    return show(request, c)

def update(request):
    logger.info('update')
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=SERVICES.getUserInfo(request.user.username))
        result = SERVICES.updateUserInfo(user_form)
        if not result == 'success':
            fail_form = UserForm(request.POST)
            c = {'form':fail_form}
            c.update({'form_message':MSGS.UPD_FAIL})
            return show(request, c)
    c = {'form_message': MSGS.UPD_SUCCESS}
    c.update({'form':user_form})
    return show(request, c)

def show(request, c):
    logger.info('show')

    main_url = CONFIG.TOP_URL
    page_title = CONFIG.ACCOUNT_PAGE_TITLE_URL
    main_content = CONFIG.ACCOUNT_MAIN_URL
    sub_content = CONFIG.ACCOUNT_SUB_URL
    action_dict = CONFIG.ACTION_DICT
    url_dict = {'main_url':main_url, 
                'page_title':page_title, 
                'main_content':main_content,
                'sub_content':sub_content}
    c.update(csrf(request))
    c.update(url_dict)
    c.update(action_dict)
    return render(request, 'common/main.html', c)
