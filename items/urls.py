from django.conf.urls import url
from items import views

urlpatterns = [
    url(r'^$', views.items, name='items'),
    url(r'^item/', views.infoitem, name='infoItem'),
    url(r'^add_item/$', views.item, name='addItem'),
    url(r'^edit_item/(?P<item_id>[0-9]+)/$', views.item, name='editItem'),
    url(r'^remove_item/(?P<item_id>[0-9]+)/$', views.removeitem, name='removeItem'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^add_category/$', views.category, name='addCategory'),
    url(r'^edit_category/(?P<category_id>[0-9]+)/$', views.category, name='editCategory'),
    url(r'^remove_category/(?P<category_id>[0-9]+)/$', views.removecategory, name='removeCategory'),
    url(r'^manufacturers/$', views.manufacturers, name='manufacturers'),
    url(r'^add_manufacturer/$', views.manufacturer, name='addManufacturer'),
    url(r'^edit_manufacturer/(?P<manufacturer_id>[0-9]+)/$', views.manufacturer, name='editManufacturer'),
    url(r'^remove_manufacturer/(?P<manufacturer_id>[0-9]+)/$', views.removemanufacturer, name='removeManufacturer')
]