# -*- coding: utf-8 -*-
from django import forms
import common.models as MODELS
from django.forms.widgets import Textarea
from common.models import Target_register

class ProgressManagementForm(forms.ModelForm):

    select_target = forms.ChoiceField(choices=())

    class Meta:
        model = MODELS.Progress_management

        # 表示したいフィールド名だけを指定する。
        fields = ('select_target',  'relationship', 'progress', 'remarks')

        # remarksのname属性をtextareaに変更
        widgets = {
            'remarks': Textarea(attrs={'cols': 40, 'rows': 10}),
        }

    def __init__(self, user, *args, **kwargs):
        super(ProgressManagementForm, self).__init__(*args, **kwargs)

        # formの__init__を上書きして、ターゲットを表示するようにする
        # 表示ターゲット：自分が登録したターゲット、チームターゲット
        # リストから除外するターゲット：自分以外が担当しているターゲット
        target_dict = [(target_register.target.id, target_register.target) for target_register in Target_register.objects.filter(user=user)]

        self.fields['select_target'] = forms.ChoiceField(choices=target_dict)
        self.fields['select_target'].label = '担当'
        self.fields['select_target'].widget.attrs['class'] = 'form-control'

        self.fields['relationship'].widget.attrs['class'] = 'form-control'
        self.fields['progress'].widget.attrs['class'] = 'form-control'
        self.fields['remarks'].widget.attrs['class'] = 'form-control'

