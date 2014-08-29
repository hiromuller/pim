# -*- coding: utf-8 -*-
'''
Created on 2014/08/14

@author: yu-yama
'''
from social.pipeline.partial import partial
import logging
logger = logging.getLogger('app')

@partial
def get_profile_photo(strategy, details, response, user=None, is_new=False, *args, **kwargs):

    logger.info(get_profile_photo)
    user.profile_photo = response['profile_image_url']

    logger.info(user.profile_photo)
    user.save()

