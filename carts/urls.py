from django.conf.urls import url
from carts import views

urlpatterns = [
    url(r'^update_cart/(?P<item_id>[0-9]+)/$', views.actualitzar_carret, name='actualitzarCarret'),
    url(r'^show_sales_order/$', views.veure_comanda, name='veureComanda'),
    url(r'^show_sales_order/cart_confirmation/$', views.confirmar_carret, name='confirmarCarret'),
    url(r'^show_sales_order/delete_line/(?P<item_id>[0-9]+)/$', views.esborrar_linia, name='esborrarLinia'),
    url(r'^show_sales_order/delete_sales_order/$', views.esborrar_comanda, name='esborrarComanda'),
    url(r'^sales_list/$', views.llista_comandes, name='llistaComandes'),
    url(r'^sales_list/order_details/(?P<comanda_id>[0-9]+)/$', views.detall_comanda, name='detallComanda')
]