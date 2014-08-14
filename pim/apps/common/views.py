# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
import services as SERVICE
import configs as CONFIG
import progress_latest.views as PROGRESS_LATEST_VIEWS
import progress_list.views as PROGRESS_LIST_VIEWS
import target_detail.views as TARGET_DETAIL_VIEWS
import target_list.views as TARGET_LIST_VIEWS
import user_detail.views as USER_DETAIL_VIEWS
import user_list.views as USER_LIST_VIEWS

#@login_required(login_url='/login/')
def show(request):
    #暫定的にsessionユーザを定義。あとで消す
    test_user = SERVICE.getUserByLoginId('user1')
    request.session['user'] = test_user
    #ここまで
    
    if request.method == "POST":
        action = request.POST["action"]
    else:
        action = CONFIG.ACTION_TOP
    
    #ページの振り分け
    if action == CONFIG.ACTION_PROGRESS_LATEST:
        return PROGRESS_LATEST_VIEWS.index(request)
    elif action == CONFIG.ACTION_PROGRESS_LIST:
        return PROGRESS_LIST_VIEWS.index(request)
    elif action == CONFIG.ACTION_TARGET_DETAIL:
        return TARGET_DETAIL_VIEWS.index(request)
    elif action == CONFIG.ACTION_TARGET_ADD:
        return TARGET_LIST_VIEWS.add(request)
    elif action == CONFIG.ACTION_TARGET_LIST:
        return TARGET_LIST_VIEWS.index(request)
    elif action == CONFIG.ACTION_USER_DETAIL:
        return USER_DETAIL_VIEWS.index(request)
    elif action == CONFIG.ACTION_USER_LIST:
        return USER_LIST_VIEWS.index(request)    
    else:
        main_url = CONFIG.TOP_URL
        page_title = action + CONFIG.PAGE_TITLE
        main_content = action + CONFIG.CONTENT_MAIN
        sub_content = action + CONFIG.CONTENT_SUB
        
        c = {}    
        url_dict = {'main_url':main_url, 
                    'page_title':page_title,
                    'main_content':main_content,
                    'sub_content':sub_content}
        c.update(csrf(request))
        c.update(url_dict)
        return render(request, 'common/main.html', c)