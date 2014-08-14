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
        