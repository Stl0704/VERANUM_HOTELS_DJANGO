from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Usuario(models.Model):
    nombreu = models.CharField(max_length=200, null=True)
    rut = models.CharField(max_length=200, null=True)
    fNac = models.DateField(null=True)
    email = models.EmailField(max_length=254, null=True)
    contrasenia = models.CharField(max_length=200, null=True)
    direccion = models.CharField(max_length=200, null=True)


class Platillo(models.Model):
    nombreP = models.CharField(max_length=200, null=True)
    descripcion = models.CharField(max_length=1000, null=True)
    ingredientes = models.CharField(max_length=500, null=True)
    precio = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    imgn_ref = models.CharField(max_length=1000, null=True)

class Servicio(models.Model):
    nombreS = models.CharField(max_length=200, null=True)
    descripcionS = models.CharField(max_length=1000, null=True)
    precioS = models.DecimalField(max_digits=12, decimal_places=2, null=True)

class Reserva (models.Model):
    fechaRev = models.DateField(null=True)
    nHab = models.IntegerField(null=False)
    totaliniRev = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    totalfinRev = models.DecimalField(max_digits=12, decimal_places=2, null=True)





# CONTINUAR CON LOS MODELOS DE RESERVA_USUARIO , PEDIDO_RESTAURANT
