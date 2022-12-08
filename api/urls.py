from django.urls import path
from . import views

urlpatterns = [
    path('catalogo', views.catalogo, name='catalogo'),
    path('catalogo/editar/<str:pk>', views.editarCatalogo, name= 'editarCatalogo'),
    path('catalogo/nuevo-producto', views.añadirNuevoProducto, name='nuevoProducto'),
    path('entradas', views.entradas, name='entradas'),
    path('salidas', views.salidas, name='salidas'),
    path('reporte-salidas', views.reporteSalidas, name='reporte-salidas'),
    path('reporte-entradas', views.reporteEntradas, name='reporte-entradas'),
    path('entradas/crear-entrada/<str:pk>', views.crearEntrada, name='crearEntrada'),
    path('salidas/crear-salida/<str:pk>', views.crearSalida, name='crearSalida'),
    path('provedores', views.Provedores, name='provedores'),
    path('provedores/nuevo-provedor', views.añadirNuevoProvedor, name='nuevoProvedor'),
    path('provedores/editar/<str:pk>', views.editarProvedor, name= 'editarProvedor'),
]