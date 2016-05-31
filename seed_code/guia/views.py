from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.contrib import messages
from .froms import PostFormConsejo

# Create your views here.
class Guia(View):
    def get(slef, request):
        template_name = 'guia/guia.html'
        form1 = PostFormConsejo()
        context = {'form1':form1}




    def displayconsejo(request, idp):
        element = models.Consejo.objects.get(pk = idc)
        return render(request, '', {'consejo': element})
