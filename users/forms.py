# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder':'Introdueix el teu usuari','autofocus':'autofocus'}))
    password = forms.CharField(min_length=5, max_length=100, widget=forms.PasswordInput(attrs={'placeholder':'Introdueix el teu password'}))

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder':'Introdueix el teu nom d\'usuari','autofocus':'autofocus'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Introdueix el teu correu electrònic'}))
    password = forms.CharField(min_length=5, max_length=100, widget=forms.PasswordInput(attrs={'placeholder':'Introdueix el teu password'}))
    repeat_password = forms.CharField(min_length=5, max_length=100, widget=forms.PasswordInput(attrs={'placeholder':'Repeteix el teu password'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('El nom d\'usuari ja està ocupat')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('El correu electrònic ja està registrat')
        return email

class ChangePasswordForm(forms.Form):
    password = forms.CharField(min_length=5, max_length=100, widget=forms.PasswordInput(attrs={'placeholder':'Introdueix el teu nou password'}))
    repeat_password = forms.CharField(min_length=5, max_length=100, widget=forms.PasswordInput(attrs={'placeholder':'Repeteix el teu nou password'}))