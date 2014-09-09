# -*- coding: utf-8 -*-
import common.models as MODELS
import logging

logger = logging.getLogger('app')

def selectTeamByUser(user):
    """
    ユーザが所属するチームのリストを返す
    """
    logger.info('selectTeamByUser')
    team_list = []
    membership_list = MODELS.Membership.objects.filter(user=user)
    if len(membership_list) >= 1:
        for membership in membership_list:
            team_list.append(membership.team)
    return team_list

def selectUsersByTeam(team):
    logger.info('selectMembersByTeam')
    """
    チームからメンバーのリストを返す
    """
    membership_list = MODELS.Membership.objects.filter(team=team)
    user_list = []
    for membership in membership_list:
        user_list.append(membership.user)
    return user_list

def addNewTeam(teamAddForm, user):

    result_flg = False
    if isUserExist(user):
        new_team = addTeam(teamAddForm)
        if new_team:
            new_membership = addNewMembership(new_team, user)
            if new_membership:
                result_flg = True

    if result_flg:
        return 'success'
    else:
        return 'fail'

def addTeam(team_add_form):

    logger.info('チーム登録')

    if team_add_form.is_valid():
        team = MODELS.Team()
        team.name = team_add_form.cleaned_data['name']
        team.save()
        return team
    else:
        return None

def addNewMembership(team, user):
    '''
    チームが新しく作成された時、管理者フラグをONにする
    '''

    logger.info('メンバーシップ登録')
    membership = MODELS.Membership()
    membership.team = team
    membership.user = user
    membership.team_admin_flg = True
    membership.save()
    return membership

def inviteUser(team_invite_form, user):
    logger.info('チーム招待')

    if team_invite_form.is_valid():
        input_user = selectUserById(team_invite_form.cleaned_data['user_id'])
        team = selectTeamById(team_invite_form.cleaned_data['team_id'])

        if team:
            user_has_membership = chkUserMemberShip(user, team)
        else:
            user_has_membership = False

        if input_user and user_has_membership:
            is_team_admin = isTeamAdmin(user, team)
            approve_by_admin_flg = False
            if is_team_admin:
                approve_by_admin_flg = True
            invitation = addInvitation(team, input_user, user, approve_by_admin_flg)
            if invitation:
                return 'success'

    return 'fail'

def addInvitation(team, invited_user, invited_by, approve_by_admin_flg):
    logger.info('addInvitation')
    invitation = MODELS.Invitation()
    invitation.team = team
    invitation.invited_user = invited_user
    invitation.invited_by = invited_by
    invitation.approve_by_admin_flg = approve_by_admin_flg
    invitation.save()

    return invitation

def selectUserById(user_id):
    logger.info('selectUserById : ' + user_id)
    try:
        user = MODELS.User.objects.get(username=user_id)
        return user
    except MODELS.User.DoesNotExist:
        return None

def selectTeamById(team_id):
    logger.info('selectTeamById : ' + team_id)
    try:
        team = MODELS.Team.objects.get(id=team_id)
        return team
    except MODELS.Team.DoesNotExist:
        return None

def isUserExist(user):
    logger.info('username = ' + user.username)

    # 投げられたusernameで存在チェックを行う
    isUserExist = MODELS.User.objects.filter(username=user.username).count()
    if isUserExist == 0:
        return False
    else:
        return True

def isTeamAdmin(user, team):
    """
    チーム管理者か確認する
    return boolean
    """
    logger.info('isTeamAdmin: ' + user.username + ', ' + team.name)

    try:
        if chkUserMemberShip(user, team):
            if MODELS.Membership.objects.get(team=team, user=user).team_admin_flg:
                return True
        return False
    except MODELS.Membership.DoesNotExist:
        return False

def chkUserMemberShip(user, team):
    """
    ユーザがチームに所属しているか確認する
    return boolean
    """
    logger.info('chkUserMemberShip: ' + user.username + ", " + team.name)

    try:
        if MODELS.Membership.objects.get(user=user, team=team):
            return True
        else:
            return False
    except MODELS.Membership.DoesNotExist:
        return False

def selectWaitingUserList(team_list):
    """
    承認街ユーザリストを取得する
    return user[]
    """
    logger.info('selectWaitingUserList')
    user_list = []
    if team_list:
        invitation_list = MODELS.Invitation.objects.filter(team=team_list[0])
        for invitation in invitation_list:
            if not invitation.approve_by_admin_flg or not invitation.approve_by_user_flg:
                user_list.append(invitation.invited_user)
    return user_list



