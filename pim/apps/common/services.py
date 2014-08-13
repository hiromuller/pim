'''
Created on 2014/07/23

@author: h-nagata
'''
from models import Target, User, Team, Progress_management

def getUserByLoginId(login_id):
    user = User.objects.filter(login_id = login_id)
    if user.count() == 1:
        return user.first().encode()
    else:
        return None