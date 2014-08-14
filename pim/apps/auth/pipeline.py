# -*- coding: utf-8 -*-
'''
Created on 2014/08/14

@author: yu-yama
'''
from social.pipeline.partial import partial

@partial
def get_profile_photo(strategy, details, response, user=None, is_new=False, *args, **kwargs):
    print "get_profile_photo"
    user.profile_photo = response['profile_image_url']
    print user.profile_photo
    user.save()

