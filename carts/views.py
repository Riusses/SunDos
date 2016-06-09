# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.forms import modelform_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from carts.models import Comanda, Linia
from items.models import Categoria, Producte
from .forms import edit_cart

def actualitzar_carret(request,item_id):
    pdt=get_object_or_404(Producte,pk=item_id)
    if request.method=='POST':
        form=edit_cart(request.POST)
        if form.is_valid():
            if 'carret' not in request.session:
                request.session['carret']={}
            qnt=form.cleaned_data['quantitat']
            if qnt>pdt.quantitat:
                messages.error(request,'No hi ha suficients existències, actualment tenim ' + unicode(pdt.quantitat) + ' unitat/s')
            else:
                request.session['carret'].update({item_id:qnt})
                messages.add_message(request,messages.SUCCESS,'El producte s\'ha afegit dins el carret')
                return HttpResponseRedirect(reverse('items:items'))
        else:
            messages.error(request,'Hi ha errors en el formulari')
    else:
        form=edit_cart()

    form.helper=FormHelper()
    return render(request,'carts/edit_cart.html',{'form':form,'producte':pdt})

def veure_comanda(request):
    if 'carret' not in request.session:
        request.session['carret']={}
    ui_cart=[]
    preu_comanda=0
    for id in request.session['carret']:
        pdt=Producte.objects.get(id=id)
        qnt=request.session['carret'][id]
        pre=pdt.preu*qnt
        preu_comanda+=pre
        ui_cart.append({'producte':pdt,
                        'quantitat':qnt,
                        'preu':pre
                        })
    return render(request,'carts/cart.html',{'ui_cart':ui_cart,'preu_comanda':preu_comanda})

def esborrar_linia(request,item_id):
    request.session.modified=True
    pdt=request.session['carret']
    if item_id in pdt:
        del pdt[item_id]
    return HttpResponseRedirect(reverse('carts:veureComanda'))

def esborrar_comanda(request):
    if 'carret' in request.session:
        request.session['carret']={}
    return HttpResponseRedirect(reverse('carts:veureComanda'))

@user_passes_test(lambda u:u.is_authenticated(), login_url='/login/')
def confirmar_carret(request):
    addConfirmCartForm=modelform_factory(Comanda,exclude=('comanda_id','usuari','data','estat'))
    cmd=Comanda()
    if request.method=='POST':
        form=addConfirmCartForm(request.POST,request.FILES,instance=cmd)
        if form.is_valid():
            carrer=form.cleaned_data['carrer']
            poblacio=form.cleaned_data['poblacio']
            codi_postal=form.cleaned_data['codi_postal']
            provincia=form.cleaned_data['provincia']
            if 'carret' in request.session:
                if request.session['carret']:
                    cmd.carrer=carrer
                    cmd.poblacio=poblacio
                    cmd.codi_postal=codi_postal
                    cmd.provincia=provincia
                    cmd.usuari=request.user
                    cmd.save()
                    crt=request.session['carret']
                    for id in crt:
                        pdt=Producte.objects.get(id=id)
                        qnt=crt[id]
                        if qnt>pdt.quantitat:
                            messages.error(request,'No hi ha suficients existències')
                            return HttpResponseRedirect(reverse('carts:veureComanda'))
                        else:
                            linia=Linia()
                            linia.comanda_id=cmd
                            linia.producte_id=pdt
                            linia.quantitat=qnt
                            linia.preu=pdt.preu
                            linia.save()
                            pdt.quantitat=pdt.quantitat-qnt
                            pdt.save()
                            request.session['carret']={}
                    return HttpResponseRedirect(reverse('carts:llistaComandes'))
                else:
                    messages.error(request,'No hi ha cap producte al carret')
            else:
                return HttpResponseRedirect(reverse('items:items'))
        else:
            messages.error(request,'Hi ha errors en el formulari')
    else:
        form=addConfirmCartForm(instance=cmd)

    form.helper=FormHelper()
    form.helper.form_class='blueForms'
    form.helper.label_class='col-lg-2'
    form.helper.field_class='col-lg-10'
    form.helper.add_input(Submit('submit','Finalitzar compra'))
    return render(request,'carts/confirmation_form.html',{'form':form})

@user_passes_test(lambda u:u.is_authenticated(), login_url='/login/')
def llista_comandes(request):
    cmd=Comanda.objects.filter(usuari=request.user)
    return render(request,'carts/sales_list.html',{'comandes':cmd})

@user_passes_test(lambda u:u.is_authenticated(), login_url='/login/')
def detall_comanda(request,comanda_id):
    preu_comanda=0
    ui_comanda=[]
    lns=Linia.objects.filter(comanda_id=comanda_id)
    for lna in lns.all():
        pdt=Producte.objects.get(id=lna.producte_id.id)
        qnt=lna.quantitat
        pre=lna.preu*qnt
        preu_comanda+=pre
        ui_comanda.append({'producte':pdt,
                           'quantitat':qnt,
                           'preu':pre
                           })
    return render(request,'carts/detail.html',{'ui_comanda':ui_comanda,'preu_comanda':preu_comanda})