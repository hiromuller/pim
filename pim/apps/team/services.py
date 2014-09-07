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
    

def isUserExist(user):
    logger.info('username = ' + user.username)

    # 投げられたusernameで存在チェックを行う
    isUserExist = MODELS.User.objects.filter(username=user.username).count()
    if isUserExist == 0:
        return False
    else:
        return True
