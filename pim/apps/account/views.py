# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.context_processors import csrf
import configs as CONFIG
import services as SERVICES
import common.models as MODELS
import logging
from account.forms import UserForm
logger = logging.getLogger('app')

def index(request):
    logger.info('index')

    print request.user.username
    user = MODELS.User.objects.get(pk=request.user.username)
    form = UserForm(instance=user)
#     form = {'form':UserForm()}

#     # 担当者の進捗一覧を取得し、返却する
#     user_info = SERVICES.getUserInfo(request.user)
    

    main_url = CONFIG.TOP_URL
    page_title = CONFIG.ACCOUNT_PAGE_TITLE_URL
    main_content = CONFIG.ACCOUNT_MAIN_URL
    sub_content = CONFIG.ACCOUNT_SUB_URL
    action_dict = CONFIG.ACTION_DICT
    c = {}
    c.update({'form':form})
    url_dict = {'main_url':main_url, 
                'page_title':page_title, 
                'main_content':main_content,
                'sub_content':sub_content}
    c.update(csrf(request))
    c.update(url_dict)
    c.update(action_dict)
    return render(request, 'common/main.html', c)