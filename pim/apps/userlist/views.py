# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.context_processors import csrf
import configs as CONFIG
import settings as SETTING
import services as SERVICES
import logging

logger = logging.getLogger('app')

def index(request):
    logger.info('最新進捗画面')
    c = {}

    userlist = SERVICES.getUserList()

    c.update({'userlist':userlist})

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