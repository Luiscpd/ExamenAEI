from django.db import models

# Create your models here.
class Habitacion(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(null=True, max_digits=7, decimal_places=2)

class DatosHuesped(models.Model):
    DPI = models.FloatField(default=0, primary_key=True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(null=True, max_length=100)

class  PrecioNoche(models.Model):
    checkin = models.DateTimeField(null=True)
    checkout = models.DateTimeField(null=True)
    quantity = models.IntegerField(null=True)    