# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.context_processors import csrf
import configs as CONFIG
import services as SERVICES
import consts as CONSTS
import logging

logger = logging.getLogger('app')

def index(request):
    logger.info('最新進捗画面')
    user = request.user
    c = {}

    main_url = CONFIG.TOP_URL
    page_title = CONFIG.HELP_PAGE_TITLE_URL
    main_content = CONFIG.HELP_MAIN_URL
    sub_content = CONFIG.HELP_SUB_URL
    action_dict = CONFIG.ACTION_DICT
#     user_dict = {'user':user}
    url_dict = {'main_url':main_url,
                'page_title':page_title,
                'main_content':main_content,
                'sub_content':sub_content}
    c.update(csrf(request))
    c.update({'html_title':CONFIG.HELP_HTML_TITLE})
    c.update(url_dict)
    c.update(action_dict)
#     c.update(user_dict)
    return render(request, 'common/main.html', c)