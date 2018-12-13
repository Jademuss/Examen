from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path('', views.index, name='index'),
    path('index.html', views.index, name='index2'),
    path('login.html', views.login, name='login'),
    path('registroProducto.html', views.registroProducto, name='registroProducto'),
    path('registroTienda.html', views.registroTienda, name='registroTienda'),
    path('listaProducto.html', views.listaProductos, name='listarProducto'),
    path('<int:pk>', views.detalleProducto, name='detalleProducto'), 
    path('validarTienda.html', views.validarTienda, name='validarTienda'),

]	