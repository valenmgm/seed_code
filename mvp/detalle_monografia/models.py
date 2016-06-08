from __future__ import unicode_literals

from django.db import models

# Create your models here.

class DetalleMonografia(models.Model):
    nombre = models.CharField(max_length= 120, blank=False)
    precioSemilla = models.DecimalField(max_digits=9, decimal_places=2)
    precioVenta = models.DecimalField(max_digits=9, decimal_places=2)
    regiones = models.TextField(max_length=500)
    #climas y temporadas
    cuidados = models.TextField(max_length=500)

    def __str__(self):
        return unicode(self.nombre)
