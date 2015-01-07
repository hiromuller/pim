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
    progress_list = []

    if user.username == 'PimClubOwner':
        progress_list.extend(SERVICES.getAllProgressList())
    else:
        # 担当者の進捗一覧を取得し、返却する
        user_progress_list = SERVICES.getUserProgressList(user)
        if len(user_progress_list) > 0:
            progress_list.extend(user_progress_list)

        # 担当者の所属するチームの別メンバの進捗を取得し、返却する
        team_progress_lists = SERVICES.getTeamProgressList(user)
        for team_progress_list in team_progress_lists:
            if len(team_progress_list) > 0:
                progress_list.extend(team_progress_list)

    if progress_list:
        progress_list = sorted(progress_list, key=lambda x:x.registered_at, reverse=True)

    if len(progress_list) > CONSTS.MAX_NUM_LATEST_PROGRESS_LIST:
        del progress_list[CONSTS.MAX_NUM_LATEST_PROGRESS_LIST:len(progress_list)]
    c.update({'progress_list':progress_list})

    main_url = CONFIG.TOP_URL
    page_title = CONFIG.HOME_PAGE_TITLE_URL
    main_content = CONFIG.HOME_MAIN_URL
    sub_content = CONFIG.HOME_SUB_URL
    action_dict = CONFIG.ACTION_DICT
#     user_dict = {'user':user}
    url_dict = {'main_url':main_url,
                'page_title':page_title,
                'main_content':main_content,
                'sub_content':sub_content,
                }
    c.update(csrf(request))
    c.update({'html_title':CONFIG.HOME_HTML_TITLE})
    c.update(url_dict)
    c.update(action_dict)
#     c.update(user_dict)
    return render(request, 'common/main.html', c)