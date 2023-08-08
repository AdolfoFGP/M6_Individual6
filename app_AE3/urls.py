from django.urls import path
from . views import lista_usuarios

app_name = 'app_AE3'

urlpatterns = [
    path("usuarios/", lista_usuarios, name='usuarios'),
]