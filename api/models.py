from django.db import models
from django.utils import timezone

# Create your models here.
class provedores(models.Model):
    name = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)
    direccion = models.CharField(max_length=100)


class Productos(models.Model):
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    codigo_barra = models.IntegerField()
    modelo = models.CharField(max_length=50)
    unidadesEnStock = models.IntegerField()
    precioUnitario = models.FloatField(default=0)
    provedor = models.ForeignKey(provedores, on_delete=models.SET_NULL, blank=True, null=True)

class Servicio(models.Model):
    nombre_servicio = models.CharField(max_length=50)
    descripcion_servicio = models.CharField(max_length=200)
    precio = models.FloatField()

class Entradas(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    producto = models.ForeignKey(Productos, on_delete=models.SET_NULL, blank=True, null=True)
    cantidad = models.IntegerField()
    provedor = models.ForeignKey(provedores, on_delete=models.SET_NULL, blank=True, null=True)

class Salidas(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    producto = models.ForeignKey(Productos, on_delete=models.SET_NULL, blank=True, null=True)
    cantidad = models.IntegerField()

class Pedidos(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.SET_NULL, blank=True, null=True)
    cantidad = models.IntegerField()
    fecha_de_orden = models.DateTimeField(default=timezone.now)
    fecha_estimada_llegada = models.DateField()
   