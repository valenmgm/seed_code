from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Consejo(models.Model):

    #Atributos
    titulo = models.CharField(max_length = 120, blank = False)
    fecha = models.DateField(auto_now_add = True)
    intruduccion = models.TextField(blank = False)
    para_que = models.TextField(blank = False)
    como = models.TextField(blank = False)

    
