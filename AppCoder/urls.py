from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio, name = "Inicio"),
    path("vista", vista, name = "Vista"),
    path("formulario", formu),
    path("buscador", busqueda),
    
]