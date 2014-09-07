# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.context_processors import csrf
import configs as CONFIG
import services as SERVICES
import models as TEAM_MODELS
import forms as FORMS
import messages as MSGS
import logging

logger = logging.getLogger('app')

# Create your views here.
def index(request):
    logger.info('チーム画面開始')  
    forms = {'teamAddForm':FORMS.TeamAddForm()}
    c = {}
    c.update(forms)
    return show(request, c)
      
def add(request):
    """
    チーム登録
    """
    logger.info('チーム登録')

    if request.method == 'POST':
        teamAddForm = FORMS.TeamAddForm(request.POST)
        result = SERVICES.addNewTeam(teamAddForm, request.user)

        if not result == 'success':
            fail_form = FORMS.TeamAddForm(request.POST)
            c = {'addForm':fail_form}
            c.update({'form_message':MSGS.ADD_FAIL})
            return show(request, c)

    c = {'form_message': MSGS.ADD_SUCCESS}
    c.update({'addForm':FORMS.TeamAddForm()})
    return show(request, c)

def show(request, c):
    """
    チームメンバー一覧画面インデックス
    最初に必ず通る
    """
    logger.info('チームメンバーリスト画面開始')
    
    team_members_list = []
    team_list = SERVICES.selectTeamByUser(request.user)
    
    for team in team_list:
        users = SERVICES.selectUsersByTeam(team)        
        team_members_list.append(TEAM_MODELS.Team_Members(team, users))
        
    c.update({'team_members_list':team_members_list})

    main_url = CONFIG.TOP_URL
    page_title = CONFIG.TEAM_PAGE_TITLE_URL
    main_content = CONFIG.TEAM_MAIN_URL
    sub_content = CONFIG.TEAM_SUB_URL

    url_dict = {'main_url':main_url, 
                'page_title':page_title, 
                'main_content':main_content,
                'sub_content':sub_content}
    c.update(csrf(request))
    c.update(url_dict)
    c.update(CONFIG.ACTION_DICT)
    return render(request, 'common/main.html', c)