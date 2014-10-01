# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
import services as SERVICE
import configs as CONFIG
import home.views as HOME_VIEWS
import progress.views as PROGRESS_VIEWS
import target.views as TARGET_VIEWS
import account.views as ACCOUNT_VIEWS
import team.views as TEAM_VIEWS
import help.views as HELP_VIEWS
import manual.views as MANUAL_VIEWS

@login_required(login_url='/login/')
def show(request):
    #暫定的にsessionユーザを定義。あとで消す
    test_user = SERVICE.getUserByLoginId('user1')
    request.session['user'] = test_user
    #ここまで

    if request.method == "POST":
        action = request.POST["action"]
    else:
        action = CONFIG.ACTION_HOME

    #ページの振り分け
    if action == CONFIG.ACTION_HOME:
        return HOME_VIEWS.index(request)

    elif action == CONFIG.ACTION_PROGRESS_LIST:
        return PROGRESS_VIEWS.index(request)

    elif action == CONFIG.ACTION_PROGRESS_ADD:
        return PROGRESS_VIEWS.add(request)

    elif action == CONFIG.ACTION_PROGRESS_UPDATE:
        return PROGRESS_VIEWS.update(request)

    elif action == CONFIG.ACTION_TARGET_LIST:
        return TARGET_VIEWS.index(request)

    elif action == CONFIG.ACTION_TARGET_ADD:
        return TARGET_VIEWS.add(request)

    elif action == CONFIG.ACTION_TARGET_DETAIL:
        return TARGET_VIEWS.targetDetail(request)

    elif action == CONFIG.ACTION_TARGET_UPDATE:
        return TARGET_VIEWS.targetUpdate(request)

    elif action == CONFIG.ACTION_ACCOUNT:
        return ACCOUNT_VIEWS.index(request)

    elif action == CONFIG.ACTION_ACCOUNT_UPDATE:
        return ACCOUNT_VIEWS.update(request)

    elif action == CONFIG.ACTION_TEAM:
        return TEAM_VIEWS.index(request)

    elif action == CONFIG.ACTION_TEAM_ADD:
        return TEAM_VIEWS.add(request)

    elif action == CONFIG.ACTION_TEAM_INVITE:
        return TEAM_VIEWS.invite(request)

    elif action == CONFIG.ACTION_TEAM_INVITE_ACCEPT_USER:
        return TEAM_VIEWS.acceptMember(request)

    elif action == CONFIG.ACTION_TEAM_INVITE_ACCEPT_TEAM:
        return TEAM_VIEWS.acceptTeam(request)

    elif action == CONFIG.ACTION_TEAM_DELETE_MEMBER:
        return TEAM_VIEWS.deleteMember(request)

    elif action == CONFIG.ACTION_TEAM_DELETE_TEAM:
        return TEAM_VIEWS.deleteTeam(request)

    elif action == CONFIG.ACTION_HELP:
        return HELP_VIEWS.index(request)

    elif action == CONFIG.ACTION_MANUAL:
        return MANUAL_VIEWS.index(request)

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
