# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_protect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from users.forms import LoginForm, RegistrationForm, ChangePasswordForm

@csrf_protect
def vista_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('items:items'))
    else:
        if request.method=='POST':
            form=LoginForm(request.POST)
            if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                seguent=request.GET.get('next',default=None)
                user=authenticate(username=username,password=password)
                if user is not None:
                    if user.is_active:
                        login(request,user)
                        if bool(seguent):
                            return HttpResponseRedirect(seguent)
                        else:
                            return HttpResponseRedirect(reverse('items:items'))
                    else:
                        messages.error(request,'Usuari desactivat')
                        return HttpResponseRedirect(reverse('login'))
                else:
                    messages.error(request,'Error, usuari i/o contrasenya són/és incorrectes/e/a')
                    return HttpResponseRedirect(reverse('login'))
            else:
                messages.error(request,'Hi ha errors en el formulari')
        else:
            form=LoginForm()

    form.helper=FormHelper()
    form.helper.form_class='form-horizontal'
    form.helper.add_input(Submit('submit','Login'))

    return render(request,'forms/login.html',{'form':form})

@csrf_protect
def vista_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('items:items'))

@csrf_protect
def vista_registre(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('items:items'))
    else:
        if request.method=='POST':
            form=RegistrationForm(request.POST)
            if form.is_valid():
                cleaned_data=form.cleaned_data
                username=cleaned_data.get('username')
                password=cleaned_data.get('password')
                email=cleaned_data.get('email')
                User.objects.create_user(username=username,password=password,email=email)
                messages.success(request,'Usuari registrat correctament')
                return HttpResponseRedirect(reverse('login'))
            else:
                messages.error(request,"Hi ha errors en el formulari")
        else:
            form=RegistrationForm()

    form.helper=FormHelper()
    form.helper.form_class='form-horizontal'
    form.helper.add_input(Submit('submit','Registrar-se'))

    return render(request,'forms/registration.html',{'form':form})

@user_passes_test(lambda u:u.is_authenticated(), login_url='/login/')
def vista_perfil(request):
    user=request.user
    context={'user':user}
    return render(request,'user.html',context)

@user_passes_test(lambda u:u.is_authenticated(), login_url='/login/')
def vista_clau(request):
    if request.method=='POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            cleaned_data=form.cleaned_data
            password=cleaned_data.get('password')
            user=request.user
            user.set_password(password)
            user.save()
            logout(request)
            messages.success(request,'La clau s\'ha modificat correctament')
            return HttpResponseRedirect(reverse('login'))
        else:
            messages.error(request,"Hi ha errors en el formulari")
    else:
        form=ChangePasswordForm()

    form.helper=FormHelper()
    form.helper.form_class='form-horizontal'
    form.helper.add_input(Submit('submit','Desar'))

    return render(request,'forms/registration.html',{'form':form})