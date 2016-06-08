from django.shortcuts import render

# Create your views here.

from detalle_monografia import models

def viewHome(request):
    infoDM = models.DetalleMonografia.objects.all()
    return render(request, 'home.html', {'dataDM':infoDM})
