# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.context_processors import csrf
import configs as CONFIG
from progress.forms import ProgressManagementForm
import forms as FORMS
import services as SERVICES
import messages as MSGS

# 
def index(request):
    print 'index'

    form = {'form':ProgressManagementForm()}
    c = {}    
    c.update(form)
    return show(request, c)


def add(request):
    if request.method == 'POST':
        result = SERVICES.addProgress(request.user, request.POST)
        if not result == 'success':
            fail_form = FORMS.ProgressManagementForm(request.POST)
            c = {'form':fail_form}
            c.update({'form_message':MSGS.ADD_FAIL})
            return show(request, c)
    c = {'form_message': MSGS.ADD_SUCCESS}
    c.update({'form':FORMS.ProgressManagementForm()})
    return show(request, c)

def show(request, c):
    print 'show'    

    # 担当者の進捗一覧を取得し、返却する
    user_progress_list = SERVICES.getUserProgressList(request.user)
    c.update({'user_progress_list':user_progress_list})

    main_url = CONFIG.TOP_URL
    page_title = CONFIG.PROGRESS_PAGE_TITLE_URL
    main_content = CONFIG.PROGRESS_MAIN_URL
    sub_content = CONFIG.PROGRESS_SUB_URL
#     form = {'form':ProgressManagementForm()}
    url_dict = {'main_url':main_url, 
                'page_title':page_title, 
                'main_content':main_content,
                'sub_content':sub_content}
    c.update(csrf(request))
    c.update(url_dict)
    c.update(CONFIG.ACTION_DICT)
    return render(request, 'common/main.html', c)