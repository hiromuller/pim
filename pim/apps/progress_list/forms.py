# -*- coding: utf-8 -*-


from django import forms
import common.models as MODELS

class ProgressManagementForm(forms.ModelForm):
    class Meta:
        model = MODELS.Progress_management
        
        # 表示したいフィールド名だけを指定する。
        fields = ('target', 'relationship', 'progress', 'remarks')