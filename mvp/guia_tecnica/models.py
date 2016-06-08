from __future__ import unicode_literals

from django.db import models

# Create your models here.

class GuiaTecnica(models.Model):
    titulo = models.CharField(max_length = 120, blank = False)
    fecha = models.DateField(auto_now_add = True)
    introduccion = models.TextField(blank = False)

    def __str__(self):
        return unicode(self.titulo)

class Listado(models.Model):

    listado = models.CharField(max_length = 120, blank = False)
    lista_de = models.ForeignKey(GuiaTecnica, related_name='listado_de')

    def __str__(self):
        return unicode(self.listado + " " + self.lista_de.titulo)


class ElementoListado(models.Model):
    elemento = models.CharField(max_length = 250)
    pertenece_a = models.ForeignKey(Listado, related_name='elemento_de')

    def __str__(self):
        return unicode(self.elemento)
