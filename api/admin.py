from django.contrib import admin
from .models import provedores,Productos,Salidas,Servicio,Entradas,Pedidos
# Register your models here.
@admin.register(provedores)
class ProvedoresAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto',)



admin.site.register(Salidas)
admin.site.register(Servicio)
admin.site.register(Entradas)
admin.site.register(Pedidos)
