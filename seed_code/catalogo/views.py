from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView
from .models import *

 
class Catalogo(ListView):
    categoria =  Categoria
    catalogo = Catalogo
    template_name = 'catalogohtml'
