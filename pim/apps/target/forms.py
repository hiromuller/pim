'''
Created on 2014/07/23

@author: h-nagata
'''
from django.db import models
from django.forms import ModelForm
import common.models as MODELS

class TargetForm(ModelForm):
    class Meta:
        model = MODELS.Target

    def __init__(self, *args, **kwargs):
        super(TargetForm, self).__init__(*args, **kwargs)

        self.fields['name_kanji'].required = False
        self.fields['name_kanji'].widget.attrs['style'] = 'width:150px'
        self.fields['name_hiragana'].required = False
        self.fields['name_hiragana'].widget.attrs['style'] = 'width:150px'
        self.fields['nick_name'].required = False
        self.fields['nick_name'].widget.attrs['style'] = 'width:150px'
        self.fields['difficulty'].required = False
        self.fields['level'].required = False
        self.fields['level'].widget.attrs['style'] = 'width:180px;'
        self.fields['purpose'].required = False
        self.fields['met_place'].required = False
        self.fields['met_situation'].required = False
        self.fields['birthday'].required = False
        self.fields['phone_number'].required = False
        self.fields['mail'].required = False
        self.fields['address'].required = False
        self.fields['occupation'].required = False
        self.fields['company'].required = False
        self.fields['hobby'].required = False
        self.fields['birth_place'].required = False
        self.fields['living_situation'].required = False
        self.fields['remarks'].required = False
        self.fields['type_1'].required = False
        self.fields['type_2'].required = False
        self.fields['type_3'].required = False
        self.fields['done_flg'].required = False
        self.fields['target_photo'].required = False
