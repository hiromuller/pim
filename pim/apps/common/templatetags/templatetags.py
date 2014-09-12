# -*- coding: utf-8 -*-
'''
Created on 2014/09/12

@author: h-nagata
'''
from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """入力から arg の値を全て取り去る"""
    return value.replace(arg, '')