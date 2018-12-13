from rest_framework import serializers
from .models import TiendasM,ProductosM

class tiendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = TiendasM  
        fields = '__all__'

class productoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductosM  
        fields = '__all__'