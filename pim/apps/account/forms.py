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
                   'status',
                   )

        widgets = {
#             'username': TextInput(attrs={'readonly':True}),
            'email': TextInput(attrs={'size':40}),
            'team_id': TextInput(attrs={'readonly':True}),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name_hiragana'].widget.attrs['class'] = 'form-control'
        self.fields['name_en'].widget.attrs['class'] = 'form-control'
        self.fields['team'].widget.attrs['class'] = 'form-control'
        self.fields['birthday'].widget.attrs['class'] = 'form-control'
        self.fields['birth_place'].widget.attrs['class'] = 'form-control'
        self.fields['target_type_1'].widget.attrs['class'] = 'form-control'
        self.fields['target_type_2'].widget.attrs['class'] = 'form-control'
        self.fields['target_type_3'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
