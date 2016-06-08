from django.db import models



class Semilla(models.Model):
	titulo = models.CharField(max_length=140,blank=True,null=True)
	cuerpo = models.TextField(null=True,blank=True)



class DetalleSemilla(models.Model):
	texto = models.ForeignKey(Semilla, related_name='detalle_semilla')
	cuerpo = models.TextField(null=True,blank=True)
