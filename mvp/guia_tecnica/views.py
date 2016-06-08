from django.shortcuts import render

# Create your views here.

def viewGuiaTecnica(request, idg):
    dataGuia = models.GuiaTecnica.get(pk = idg)
    return render(request, 'url_guia_tecnica', {'data':dataGuia})
