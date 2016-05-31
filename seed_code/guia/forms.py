from django import forms
from .models import Consejo

class PostFormConsejo(forms.ModelForm):
    class Meta:
        model = Consejo
        fields = ['titutlo', 'fecha', 'intruduccion', 'para_que', 'como']
