# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.context_processors import csrf
import configs as CONFIG
import settings as SETTING
import services as SERVICES
import models as TEAM_MODELS
import forms as FORMS
import messages as MSGS
import logging

logger = logging.getLogger('app')

# Create your views here.
def index(request):
    logger.info('チーム画面開始')
    c = {}

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
            c = {'teamAddForm':fail_form}
            c.update({'form_message':MSGS.ADD_FAIL})
            return show(request, c)

    c = {'form_message': MSGS.ADD_SUCCESS}
    return show(request, c)

def invite(request):
    """
    チーム招待
    """
    logger.info('チーム招待')
    c = {}

    if request.method == 'POST':
        team_invite_form = FORMS.TeamInviteForm(request.POST)
        result = SERVICES.inviteUser(team_invite_form, request.user)

        if not result == 'success':
            fail_form = FORMS.TeamInviteForm(request.POST)
            c = {'teamInviteForm':fail_form}
            c.update({'form_message':MSGS.INVITE_FAIL})
            return show(request, c)

    c = {'form_message': MSGS.INVITE_SUCCESS}

    return show(request, c)

def acceptMember(request):
    """
    チームに招待されたユーザを管理者が承認する
    """
    logger.info('チーム招待管理者承認')
    c = {}
    if request.method == "POST":
        invited_username = request.POST["invited_username"]

    print invited_username
    if invited_username:
        invited_user = SERVICES.selectUserById(invited_username)
        if invited_user is None:
            c.update({'form_message':MSGS.INVITE_ACCEPT_FAIL})
            return show(request, c)
    else:
        c.update({'form_message':MSGS.INVITE_ACCEPT_FAIL})
        return show(request, c)

    result = SERVICES.acceptMember(invited_user, SERVICES.selectTeamsByUser(request.user)[0])

    if result == 'success':
        c.update({'form_message': MSGS.INVITE_ACCEPT_SUCCESS})
    else:
        c.update({'form_message':MSGS.INVITE_ACCEPT_FAIL})

    return show(request, c)

def acceptTeam(request):
    """
    チームに招待された被招待者が承認する
    """
    logger.info('チーム招待被招待者承認')
    c = {}
    if request.method == "POST":
        team_id = request.POST["team_id"]

    if team_id:
        team = SERVICES.selectTeamById(team_id)
        if team is None:
            return index(request)
    else:
        return index(request)

    result = SERVICES.acceptTeamInvited(request.user, team)

    if result == 'success':
        c.update({'form_message': MSGS.INVITE_ACCEPT_SUCCESS})
    else:
        c.update({'form_message':MSGS.INVITE_ACCEPT_FAIL})


    return show(request, c)

def deleteMember(request):
    """
    チームからメンバーを削除する
    """
    logger.info('チームメンバ^－削除')
    c = {}

    if request.method == "POST":
        username = request.POST["object_id"]
        team_id = request.POST["delete_from_id"]

    user = SERVICES.selectUserById(username)
    team = SERVICES.selectTeamById(team_id)

    if user and team:
        result = SERVICES.deleteMember(user, team)

    if result == 'success':
        c.update({'list_form_message': MSGS.DELETE_MEMBER_SUCCESS})
    else:
        c.update({'list_form_message':MSGS.DELETE_MEMBER_FAIL})


    return show(request, c)

def deleteTeam(request):
    """
    チームを削除する
    """
    logger.info('チーム削除')
    c = {}

    if request.method == "POST":
        team_id = request.POST["object_id"]

    team = SERVICES.selectTeamById(team_id)

    if team:
        result = SERVICES.deleteTeam(team)

    if result == 'success':
        c.update({'team_delete_message': MSGS.DELETE_MEMBER_SUCCESS})
    else:
        c.update({'team_delete_message':MSGS.DELETE_MEMBER_FAIL})

    return show(request, c)

def show(request, c):
    """
    チームメンバー一覧画面インデックス
    最初に必ず通る
    """
    logger.info('チームメンバーリスト画面開始')

    team_list = SERVICES.selectTeamsByUser(request.user)

    # 一覧表示用チームメンバーリスト作成
    team_members_list = generateTeamMembersList(team_list)
    c.update({'team_members_list':team_members_list})

    # テンプレートに渡すフォームを作成する
    forms = generateForms(team_list, request.user)
    c.update(forms)

    # 承認待ちユーザリストを作成する
    waiting_user_list = SERVICES.selectWaitingUserList(team_list)
    c.update({'waiting_user_list':waiting_user_list})

    main_url = CONFIG.TOP_URL
    page_title = CONFIG.TEAM_PAGE_TITLE_URL
    main_content = CONFIG.TEAM_MAIN_URL
    sub_content = CONFIG.TEAM_SUB_URL

    url_dict = {'main_url':main_url,
                'page_title':page_title,
                'main_content':main_content,
                'sub_content':sub_content}
    c.update({'master_user_name':SETTING.MASTER_USER_NAME})
    c.update(csrf(request))
    c.update({'html_title':CONFIG.TEAM_HTML_TITLE})
    c.update(url_dict)
    c.update(CONFIG.ACTION_DICT)
    return render(request, 'common/main.html', c)

def generateTeamMembersList(team_list):
    """
    表示用チームメンバーリストを作成する
    """
    team_members_list = []
    for team in team_list:
        users = SERVICES.selectUsersByTeam(team)
        team_members_list.append(TEAM_MODELS.Team_Members(team, users))

    return team_members_list

def generateForms(team_list, user):
    """
    チームに所属しているか判定する。所属していない場合、チーム登録フォームを渡す
    所属している場合、招待フォームを渡す
    return forms{}
    """
    forms = {}
    if team_list:
        forms.update({'teamInviteForm':FORMS.TeamInviteForm(initial={'team_id':team_list[0].id})})
        forms.update({'has_team':True})
    else:
        forms.update({'teamAddForm':FORMS.TeamAddForm()})

    # 承認待ちユーザ管理者用
    if team_list:
        if SERVICES.isTeamAdmin(team_list[0], user):
            admin_approval_waiting_user_list = SERVICES.selectAdminApprovalWaitingUserList(team_list[0])
            forms.update({'admin_approval_waiting_user_list':admin_approval_waiting_user_list})

    # 承認待ちチーム被招待者用
    inviting_team_list = SERVICES.selectInvitingTeamList(user)
    forms.update({'inviting_team_list':inviting_team_list})

    return forms

