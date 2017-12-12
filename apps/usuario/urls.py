from django.conf.urls import url

from apps.usuario.views import RegistroUsuario, UserApi

urlpatterns = [
	url(r'^registrar', RegistroUsuario.as_view(), name="registrar"),
	url(r'^api', UserApi.as_view(), name="api"),

]
