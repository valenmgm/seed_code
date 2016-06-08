from django import forms
from .models import Consejo, Listado, ElementosConsejo

class ConsejoForm(forms.ModelForm):
	class Meta:
		model = Consejo
		fields = ['titulo' ,'fecha', 'introduccion', 'para_que', 'como']

class ListadoForm(forms.ModelForm):
	class Meta:
		model = Listado
		fields = ['listado','lista_de']


class ElementosConsejoForm(forms.ModelForm):
	class Meta:
		model = ElementosConsejo
		fields = ['elemento','pertenece_a']                
