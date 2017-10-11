from django.contrib import admin
from django.contrib import admin
from catalogo.models import Categoria
from catalogo.models import Oficina
from catalogo.models import Alquiler
from catalogo.models import Cliente
from catalogo.models import DetalleAlquiler


# Register your models here.


admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Oficina)


class AlquilerAdmin(admin.ModelAdmin):
    """docstring for AlquilerAdmin"""
    list_per_page = 2
    list_display = ("FechaAlta", "FechaIngreso","detalleAlquiler")
    search_fields = ("FechaAlta", "FechaIngreso",)

    def DetalleAlquiler(self, obj):
        return obj.DetalleAlquiler

   

admin.site.register(Alquiler, AlquilerAdmin)

class DetalleAlquilerAdmin(admin.ModelAdmin):
    """docstring for DetalleAlquilerAdmin"""
    list_per_page = 2
    list_display = ("cliente", "oficina","total", "Trabajador")
    search_fields = ("cliente", "oficina",)

    def Cliente(self, obj):
        return obj.Cliente

    def Oficina(self, obj):
        return obj.Oficina

    def Trabajador(self, obj):
        return obj.Trabajador

   

admin.site.register(DetalleAlquiler, DetalleAlquilerAdmin)





