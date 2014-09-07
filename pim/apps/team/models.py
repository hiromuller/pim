# -*- coding: utf-8 -*-

# Create your models here.

class Team_Members(object):
    """
    チーム画面のリストに表示する1チームに対するモデル
    """
    def __unicode__(self):
        return self.username
    
    def __init__(self, team, members):
        self.team = team
        self.members = members
    