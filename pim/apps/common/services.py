'''
Created on 2014/07/23

@author: h-nagata
'''
from models import Target, User, Team, Progress_management

def getUserByLoginId(username):
    user = User.objects.filter(username = username)
    if user.count() == 1:
        return user.first().encode()
    else:
        return None