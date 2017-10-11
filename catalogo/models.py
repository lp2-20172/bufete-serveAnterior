from django.db import models
from core.models import User, Persona, Trabajador



class Categoria(models.Model):

    nombre = models.CharField(max_length=60)
    detalle = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return '%s' % (self.nombre)

class Oficina(models.Model):

    codigo = models.CharField(max_length=10,null=True, blank=True)
    estado = models.CharField(null=True, max_length=10, blank=True)
    
    detalle = models.TextField(null=True, blank=True)
    precio = models.CharField(null=True, max_length=10, blank=True)
    

    categoria = models.ManyToManyField(
        "Categoria",
        verbose_name="list of Categorias",
        null=True,  blank=True)

    class Meta:
        verbose_name = "Oficina"
        verbose_name_plural = "Oficinas"

    def __str__(self):
        return '%s' % (self.codigo)



class Cliente(models.Model):

    ruc = models.CharField(max_length=10, blank=True)
    cliente = models.OneToOneField(Persona)
    

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return '%s' % (self.cliente)

class DetalleAlquiler(models.Model):

    boleta = models.CharField(null=True, max_length=10, blank=True)
    factura = models.CharField(null=True, max_length=10, blank=True)
    total = models.FloatField(default=0)

    cliente = models.ForeignKey(Cliente)
    Trabajador = models.ForeignKey(User)
    oficina = models.ForeignKey(Oficina)
       


    class Meta:
        verbose_name = "DetalleAlquiler"
        verbose_name_plural = "DetalleAlquileres"

    def __str__(self):
        return '%s' % (self.oficina)

class Alquiler(models.Model):

    FechaAlta = models.DateField(null=True)
    FechaIngreso = models.DateField(null=True)
    
    detalleAlquiler = models.ForeignKey(DetalleAlquiler)
       

    class Meta:
        verbose_name = "Alquiler"
        verbose_name_plural = "Alquileres"

    def __str__(self):
        return '%s' % (self.defetalleAlquiler)