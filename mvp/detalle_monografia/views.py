from django.shortcuts import render

# Create your views here.

def viewDetalleMonografia(request, idm):
    dataDetalle = models.DetalleMonografia.get(pk = idm)
    return render(request, 'url_detalle_monografia', {'data':dataDetalle})
