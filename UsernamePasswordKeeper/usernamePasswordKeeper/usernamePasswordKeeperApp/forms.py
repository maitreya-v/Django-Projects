from django import forms
from django.forms import PasswordInput
from django.shortcuts import render
from .models import Keeper
from django.db import models
from django.core import validators

class KeeperForm(forms.ModelForm):
    class Meta:
        model=Keeper
        fields=['user_name','password','platform']
        widgets={
            'user_name':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
            'platform':forms.TextInput(attrs={'class':'form-control'})
        }
        