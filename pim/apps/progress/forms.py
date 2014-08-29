# -*- coding: utf-8 -*-
from django import forms
import common.models as MODELS
from django.forms.widgets import Textarea

class ProgressManagementForm(forms.ModelForm):
    class Meta:
        model = MODELS.Progress_management
        
        # 表示したいフィールド名だけを指定する。
        fields = ('target', 'relationship', 'progress', 'remarks')
        
        # remarksのname属性をtextareaに変更
        widgets = {
            'remarks': Textarea(attrs={'cols': 40, 'rows': 10}),
        }