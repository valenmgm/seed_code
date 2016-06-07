from __future__ import unicode_literals

from django.db import models

class Categoria(model.Model):
	titulo = models.CharField(max_length = 120, blank = True, null=True)
	def __str__(self):
		return unicode(self.titulo)

class Catalogo(models.Model):
	#Atributos
	titulo = models.CharField(max_length = 120, blank = True, null = True)
	categoria = models.ForeignKey(Categoria, related_name='categoria')
	texto = models.TextField(blank =True, null=True)

def __str__(self):
        return unicode(self.titulo)
