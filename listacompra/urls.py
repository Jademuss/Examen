from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path('', views.index, name='index'),
    path('index/login/', views.login, name='login'),
    path('index/registroProducto/', views.registroProducto, name='registroProducto'),
    path('index/detalleProducto/<int:pk>/', views.detalleProducto, name='detalleProducto'), 
    path('index/registroTienda/', views.registroTienda, name='registroTienda'),
    path('index/detalleTienda/<int:pk>/', views.detalleTienda, name='detalleTienda'),
    path('index/listaProducto/', views.listaProductos, name='listaProducto'),
    path('index/validarTienda/', views.validarTienda, name='validarTienda'),

]	