'''
Created on 2014/07/23

@author: h-nagata
'''
from django import forms

class TeamAddForm(forms.Form):
    name = forms.CharField(max_length=50)
