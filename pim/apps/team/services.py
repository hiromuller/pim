# -*- coding: utf-8 -*-
import common.models as MODELS
import logging

logger = logging.getLogger('app')

def selectTeamsByUser(user):
    """
    ユーザが所属するチームのリストを返す
    """
    logger.info('selectTeamsByUser')
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
            new_membership = addMembership(new_team, user, True)
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

def addMembership(team, user, admin_flg):
    '''
    チームが新しく作成された時、管理者フラグをONにする
    '''
    logger.info('メンバーシップ登録')
    membership = MODELS.Membership()
    membership.team = team
    membership.user = user
    membership.team_admin_flg = admin_flg
    membership.save()
    return membership

def inviteUser(team_invite_form, user):
    logger.info('チーム招待')

    if team_invite_form.is_valid():

        do_next = True

        # 被招待者存在確認
        input_user = selectUserById(team_invite_form.cleaned_data['user_id'])

        # 被招待者がどのチームにも所属していないことを確認
        if hasTeam(input_user):
            do_next = False

        # チーム存在確認及びユーザメンバーシップ確認
        if do_next:
            team = selectTeamById(team_invite_form.cleaned_data['team_id'])

            if not team:
                do_next = False

        if do_next:
            if isTeamAdmin(team, user):
                approve_by_admin_flg = True
            else:
                approve_by_admin_flg = False
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

def acceptMember(invited_user, team):
    """
    管理者承認待ちユーザを承認する
    return success or fail
    """
    logger.info('acceptMember')
    invitation_list = MODELS.Invitation.objects.filter(team=team, invited_user=invited_user)
    if len(invitation_list) == 1:
        invitation = invitation_list[0]
        invitation.approve_by_admin_flg = True
        invitation.save()
        if invitation.approve_by_user_flg is True:
            addMembership(team, invited_user, False)
    else:
        return 'fail'

    return 'success'

def acceptTeamInvited(user, team):
    """
    被招待者がチームからの招待を承認する
    return success or fail
    """
    logger.info('acceptTeamInvite')
    invitation_list = MODELS.Invitation.objects.filter(team=team, invited_user=user)
    if len(invitation_list) == 1:
        invitation = invitation_list[0]
        invitation.approve_by_user_flg = True
        invitation.save()
        if invitation.approve_by_admin_flg is True:
            addMembership(team, user, False)
    else:
        return 'fail'

    return 'success'

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

def isTeamAdmin(team, user):
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

def selectTeamAdmin(team):
    """
    チーム管理者を取得する
    return user
    """
    logger.info('selectTeamAdmin: ' + team.name)

    return MODELS.User.objects.get(membership__team = team, membership__team_admin_flg = True)

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

def hasTeam(user):
    """
    ユーザがチームに所属しているか確認する
    return boolean
    """
    logger.info('hasTeam: '  + user.username)

    if len(MODELS.Membership.objects.filter(user=user)) == 0:
        logger.info('False')
        return False
    else:
        logger.info('True')
        return True

def selectWaitingUserList(team_list):
    """
    承認待ちユーザリストを取得する
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

def selectAdminApprovalWaitingUserList(team):
    """
    管理者承認待ちユーザリストを取得する
    return user[]
    """
    logger.info('selectAdminApprovalWaitingUserList: ' + team.name)

    user_list = []
    invitation_list = MODELS.Invitation.objects.filter(team=team, approve_by_admin_flg=False)

    for invitation in invitation_list:
        user_list.append(invitation.invited_user)
    return user_list

def selectInvitingTeamList(user):
    """
    被招待者承認待ちの招待を取得する
    return team[]
    """
    logger.info('selectInvitingTeam: ' + user.username)

    team_list = MODELS.Team.objects.filter(invitation__invited_user=user, invitation__approve_by_user_flg=False)
    return team_list

def deleteMember(user, team):
    """
    チームからメンバーを削除する
    return success or fail
    """
    logger.info('deleteMember: ' + user.username + ', ' + team.name)
    try:
        MODELS.Invitation.objects.get(invited_user = user, team = team).delete()
        MODELS.Membership.objects.get(user = user, team = team).delete()
        return 'success'
    except:
        return 'fail'