# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.management import call_command
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
import datetime
import sys
import os.path

@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def export_xml(request):
    sysout=sys.stdout
    Fitxer="backups/XML/"+str(datetime.datetime.now()).replace(" ","").replace(":","-")+".xml"
    sys.stdout=open(Fitxer,'w')
    call_command('dumpdata',indent=2,format='xml')
    sys.stdout=sysout
    messages.success(request,u'La còpia XML s\'ha generat correctament')
    return HttpResponseRedirect(reverse('items:items'))

@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def import_xml(request):
    sysin=sys.stdin
    Fitxer="backups/XML_recovery/recover.xml"
    if os.path.isfile(Fitxer):
        sys.stdin=open(Fitxer,'r')
        call_command('loaddata',Fitxer)
        sys.stdin=sysin
        messages.success(request,u'La còpia XML s\'ha copiat correctament')
        return HttpResponseRedirect(reverse('items:items'))
    else:
        messages.error(request,u'La còpia XML no s\'ha copiat correctament, no es troba l\'arxiu')
        return HttpResponseRedirect(reverse('items:items'))