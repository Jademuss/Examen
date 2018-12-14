from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),    
    path('index', views.index, name='index'),
    path('index/registroProducto/', views.registroProducto, name='registroProducto'),
    path('index/detalleProducto/<int:pk>/', views.detalleProducto, name='detalleProducto'), 
    path('index/registroTienda/', views.registroTienda, name='registroTienda'),
    path('index/detalleTienda/<int:pk>/', views.detalleTienda, name='detalleTienda'),
    path('index/listaProducto/', views.listaProductos, name='listaProducto'),
    path('index/validarTienda/', views.validarTienda, name='validarTienda'),

]	