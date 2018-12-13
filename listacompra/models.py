from django.db import models
from django.utils import timezone

class ProductosM(models.Model):
    nombre              = models.CharField(max_length=30)
    id_producto         = models.AutoField(primary_key=True)
    image_producto      = models.ImageField(blank=True,null=True,upload_to = "producto/%Y/%m/$d/")
    costo_presupuestado = models.PositiveIntegerField()
    costo_real          = models.PositiveIntegerField()
    tienda_compra       = models.CharField(max_length=20)
    notas               = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class TiendasM(models.Model):
    nombre              = models.CharField(max_length=20)
    id_tienda           = models.AutoField(primary_key=True)
    image_tienda        = models.ImageField(blank=True,null=True, upload_to = "tienda/%Y/%m/$d/")
    sucursal            = models.CharField(max_length=20)
    direccion           = models.CharField(max_length=30)
    ciudad              = models.CharField(max_length=20)
    region              = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre