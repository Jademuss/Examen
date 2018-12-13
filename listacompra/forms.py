from django import forms
from .models import TiendasM, ProductosM
""""from django.contrib.auth.models import User"""

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = ProductosM
        fields = ['nombre','image_producto','costo_presupuestado','costo_real','tienda_compra','notas' ]
        
class TiendaForm(forms.ModelForm):
    
    class Meta:
        model = TiendasM
        fields  = ['nombre','sucursal','direccion','ciudad','region',]
