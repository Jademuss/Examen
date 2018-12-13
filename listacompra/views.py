from django.shortcuts import render
from .models import TiendasM,ProductosM
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import ProductoForm, TiendaForm
from django.template import loader
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  
from .serializers import productoSerializer,tiendaSerializer

def index(request):
    return render(request, 'listacompra/index.html')

def listaProductos(request):
    lista_de_productos = ProductosM.objects.all()
    context = {'lista_de_productos': lista_de_productos}
    return render(request, 'listacompra/listaProducto.html',context)

def login(request):
    return render(request, 'listacompra/login.html')

def detalleProducto(request,pk):
    producto = get_object_or_404(ProductosM,pk=pk)
    context = {'producto':producto}
    return render (request, 'listacompra/detalleProducto.html',context)   

def registroProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST,request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            return redirect('detalleProducto',pk=producto.pk)
    else:
        form = ProductoForm()
    context = {'form':form}
    return render(request, 'listacompra/registroProducto.html',context)

def registroTienda(request):
    if request.method == 'POST':
        form = TiendaForm(request.POST,request.FILES)
        if form.is_valid():
            tienda = form.save(commit=False)
            tienda.save()
            return redirect('detalleTienda',pk=tienda.pk)
    else:
        form = TiendaForm()
    context = {'form':form}
    return render(request, 'listacompra/registroTienda.html',context)


def validarTienda(request):
    return render(request, 'listacompra/validarTienda.html')