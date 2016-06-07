from django.conf.urls import url
from . import views


urlpatterns=[
	url(r'^$',
		views.Detalle_mono.as_view(),
		name="detalle_mono"),
	
]