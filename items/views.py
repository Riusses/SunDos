from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import ensure_csrf_cookie
from django.forms import modelform_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from items.models import Categoria, Fabricant, Producte
import json

@ensure_csrf_cookie
def items(request):
    items_list=Producte.objects.all()
    context={'items_list':items_list}
    return render(request,'items/items.html',context)

def infoitem(request):
    info=json.loads(request.body)
    item=Producte.objects.get(pk=info['id'])
    infoitem={'nom':item.nom,'resum':item.resum,'video':item.video}
    resposta=json.dumps({'resposta':infoitem});
    return HttpResponse(resposta,content_type='application/json');

@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def categories(request):
    categories_list=Categoria.objects.all()
    context={'categories_list':categories_list}
    return render(request,'items/categories.html',context)

@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def manufacturers(request):
    manufacturers_list=Fabricant.objects.all()
    context={'manufacturers_list':manufacturers_list}
    return render(request,'items/manufacturers.html',context)

@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def item(request,item_id=None):
    esModificacio=(item_id!=None)
    addItemForm=modelform_factory(Producte,exclude=())
    if esModificacio:
        item=get_object_or_404(Producte,pk=item_id)
    else:
        item=Producte()
    if request.method=='POST':
        form=addItemForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            item=form.save()
            messages.success(request,'El producte s\'ha desat correctament')
            return HttpResponseRedirect(reverse('items:items'))
        else:
            messages.error(request,'Hi ha errors en el formulari')
    else:
        form=addItemForm(instance=item)

    form.helper=FormHelper()
    form.helper.form_class='blueForms'
    form.helper.label_class='col-lg-2'
    form.helper.field_class='col-lg-10'
    form.helper.add_input(Submit('submit','Desar'))
    return render(request,'forms/form.html',{'form':form})

@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def category(request,category_id=None):
    esModificacio=(category_id!=None)
    addCategoryForm=modelform_factory(Categoria,exclude=())
    if esModificacio:
        category=get_object_or_404(Categoria,pk=category_id)
    else:
        category=Categoria()
    if request.method=='POST':
        form=addCategoryForm(request.POST,request.FILES,instance=category)
        if form.is_valid():
            category=form.save()
            messages.success(request,'La categoria s\'ha desat correctament')
            return HttpResponseRedirect(reverse('items:categories'))
        else:
            messages.error(request,'Hi ha errors en el formulari')
    else:
        form=addCategoryForm(instance=category)

    form.helper=FormHelper()
    form.helper.form_class='blueForms'
    form.helper.label_class='col-lg-2'
    form.helper.field_class='col-lg-10'
    form.helper.add_input(Submit('submit','Desar'))
    return render(request,'forms/form.html',{'form':form})

@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def manufacturer(request,manufacturer_id=None):
    esModificacio=(manufacturer_id!=None)
    addManufacturerForm=modelform_factory(Fabricant,exclude=())
    if esModificacio:
        manufacturer=get_object_or_404(Fabricant,pk=manufacturer_id)
    else:
        manufacturer=Fabricant()
    if request.method=='POST':
        form=addManufacturerForm(request.POST,request.FILES,instance=manufacturer)
        if form.is_valid():
            manufacturer=form.save()
            messages.success(request,'El fabricant s\'ha desat correctament')
            return HttpResponseRedirect(reverse('items:manufacturers'))
        else:
            messages.error(request,'Hi ha errors en el formulari')
    else:
        form=addManufacturerForm(instance=manufacturer)

    form.helper=FormHelper()
    form.helper.form_class='blueForms'
    form.helper.label_class='col-lg-2'
    form.helper.field_class='col-lg-10'
    form.helper.add_input(Submit('submit','Desar'))
    return render(request,'forms/form.html',{'form':form})

@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def removeitem(request,item_id):
    item=get_object_or_404(Producte,pk=item_id)
    messages.success(request,'El producte s\'ha eliminat correctament')

    item.delete()
    return HttpResponseRedirect(reverse('items:items'))

@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def removecategory(request,category_id):
    category=get_object_or_404(Categoria,pk=category_id)
    messages.success(request,'La categoria s\'ha eliminat correctament')

    category.delete()
    return HttpResponseRedirect(reverse('items:categories'))

@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def removemanufacturer(request,manufacturer_id):
    manufacturer=get_object_or_404(Fabricant,pk=manufacturer_id)
    messages.success(request,'El fabricant s\'ha eliminat correctament')

    manufacturer.delete()
    return HttpResponseRedirect(reverse('items:manufacturers'))