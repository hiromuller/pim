# -*- coding: utf-8 -*-
from django import forms
import common.models as MODELS
from django.forms.widgets import Textarea, TextInput

class UserForm(forms.ModelForm):
    class Meta:
        model = MODELS.User

        # 表示したいフィールド名だけを指定する。
#         fields = ('target', 'relationship', 'progress', 'remarks')
         
        # remarksのname属性をtextareaに変更
        widgets = {
            'username': TextInput(attrs={'readonly':True}),
        }