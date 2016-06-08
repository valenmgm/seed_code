from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.contrib import messages
from .forms import ConsejoForm

# Create your views here.
class Guia(View):
    
    def get(self, request):
        template_name = 'guia/guia.html'
        form1 = ConsejoForm()
        context = {'form1':form1}
		return render(request,template_name,context)
	def post(self,request):
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('home')
    

    def displayconsejo(request, idp):
        element = models.Consejo.objects.get(pk = idc)
        return render(request, '', {'consejo': element})
