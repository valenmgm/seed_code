"""mvp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from guia_tecnica import viewsGT
from detalle_monografia import viewsDM
from menus import viewsM

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', viewsM.viewHome, name='url_home'),
    url(r'^detalle_monografia/(?P<idm>[0-9]+)/$', viewsDM.viewDetalleMonografia, name="url_detalle_monografia"),
    url(r'^guia_tecnica/(?P<idg>[0-9]+)/$', viewsGT.viewGuiaTecnica, name="url_guia_tecnica"),
]
