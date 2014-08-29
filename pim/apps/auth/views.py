# -*- coding: utf-8 -*-

from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
import logging
logger = logging.getLogger('app')

def logged_in(request):
    context = {}

    logger.info('logged_in')
    template = 'auth/logged_in.html'
    return render(request, template, context)

def logout(request):
    logger.info('logout')

    auth_logout(request)
    return redirect('/login')
#     return render_to_response('logged_in.html', {}, RequestContext(request))

#     context = {}
#     template = 'done.html'
#     return render(request, template, context)
