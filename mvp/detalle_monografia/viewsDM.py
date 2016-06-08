from django.shortcuts import render

from . import models
# Create your views here.

def viewDetalleMonografia(request, idm):
    dataDetalle = models.DetalleMonografia.objects.get(pk = idm)
    return render(request, 'detalle_monografia.html', {'data':dataDetalle})
