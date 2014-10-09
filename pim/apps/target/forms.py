# -*- coding: utf-8 -*-
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

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = '名前'
        self.fields['reading'].widget.attrs['class'] = 'form-control'
        self.fields['reading'].widget.attrs['placeholder'] = 'よみかた'
        self.fields['purpose'].widget.attrs['class'] = 'form-control'
        self.fields['met_date'].widget.attrs['class'] = 'form-control'
        self.fields['nick_name'].required = False
        self.fields['nick_name'].widget.attrs['class'] = 'form-control'
        self.fields['nick_name'].widget.attrs['placeholder'] = 'ニックネーム'
        self.fields['difficulty'].required = False
        self.fields['difficulty'].widget.attrs['class'] = 'form-control'
        self.fields['level'].widget.attrs['class'] = 'form-control'
        self.fields['met_place'].required = False
        self.fields['met_place'].widget.attrs['class'] = 'form-control'
        self.fields['met_situation'].required = False
        self.fields['met_situation'].widget.attrs['class'] = 'form-control'
        self.fields['birthday'].required = False
        self.fields['birthday'].widget.attrs['class'] = 'form-control'
        self.fields['birthday'].widget.attrs['placeholder'] = 'yyyy-mm-dd'
        self.fields['phone_number'].required = False
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['mail'].required = False
        self.fields['mail'].widget.attrs['class'] = 'form-control'
        self.fields['address'].required = False
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['occupation'].required = False
        self.fields['occupation'].widget.attrs['class'] = 'form-control'
        self.fields['company'].required = False
        self.fields['company'].widget.attrs['class'] = 'form-control'
        self.fields['hobby'].required = False
        self.fields['hobby'].widget.attrs['class'] = 'form-control'
        self.fields['birth_place'].required = False
        self.fields['birth_place'].widget.attrs['class'] = 'form-control'
        self.fields['living_situation'].required = False
        self.fields['living_situation'].widget.attrs['class'] = 'form-control'
        self.fields['remarks'].required = False
        self.fields['remarks'].widget.attrs['class'] = 'form-control'
        self.fields['type_1'].required = False
        self.fields['type_1'].widget.attrs['class'] = 'form-control'
        self.fields['type_2'].required = False
        self.fields['type_2'].widget.attrs['class'] = 'form-control'
        self.fields['type_3'].required = False
        self.fields['type_3'].widget.attrs['class'] = 'form-control'
        self.fields['taken_flg'].required = False
        self.fields['done_flg'].required = False
        self.fields['target_photo'].required = False
        self.fields['target_photo'].widget.attrs['class'] = 'form-control'
