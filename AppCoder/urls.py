from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio, name = "Inicio"),
    path("formSerie", formuSerie, name = "FormSerie"),
    path("formPeli", formuPeli, name = "FormPeli"),
    path("formUsuario", formu, name = "FormUsuario"),
    path("buscador/", buscarUsuario, name = "Buscador"),
    
]