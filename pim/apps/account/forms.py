# -*- coding: utf-8 -*-
from django import forms
import common.models as MODELS
from django.forms.widgets import TextInput

class UserForm(forms.ModelForm):
    class Meta:
        model = MODELS.User

        # 除外したいフィールド名を指定する。
        exclude = (
                   'username',
                   'last_login',
                   'profile_photo',
                   'is_active',
                   )
         
        widgets = {
#             'username': TextInput(attrs={'readonly':True}),
            'email': TextInput(attrs={'size':40}),
            'team_id': TextInput(attrs={'readonly':True}),
        }