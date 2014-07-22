# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import logout as auth_logout
from django.http.response import HttpResponseRedirect
from django.template.context import RequestContext

# Create your views here.
def logged_in(request):
    context = {}
    template = 'auth/logged_in.html'
    return render(request, template, context)

def done(request):
    context = {}
    template = 'auth/done.html'
    return render(request, template, context)

def logout(request):
    auth_logout(request)
    return redirect('/login')
#     return render_to_response('logged_in.html', {}, RequestContext(request))

#     context = {}
#     template = 'done.html'
#     return render(request, template, context)
