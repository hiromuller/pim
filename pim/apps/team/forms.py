'''
Created on 2014/07/23

@author: h-nagata
'''
from django import forms

class TeamAddForm(forms.Form):
    name = forms.CharField(max_length=50)

    def __init__(self, *args, **kwargs):
        super(TeamAddForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'

class TeamInviteForm(forms.Form):
    team_id = forms.CharField(max_length=50, widget=forms.HiddenInput())
    user_id = forms.CharField(max_length=200)

    def __init__(self, *args, **kwargs):
        super(TeamInviteForm, self).__init__(*args, **kwargs)

        self.fields['user_id'].widget.attrs['class'] = 'form-control'
