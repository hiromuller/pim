# -*- coding: utf-8 -*-

# Create your models here.
import services as SERVICES

class Team_Members(object):
    """
    チーム画面のリストに表示する1チームに対するモデル
    """
    def __unicode__(self):
        return self.username

    def __init__(self, team, members):
        self.team = team
        self.members = members
        self.team_admin = SERVICES.selectTeamAdmin(team)
