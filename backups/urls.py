from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^export_xml/$', views.export_xml, name='exportXML'),
    url(r'^import_xml/$', views.import_xml, name='importXML')
]