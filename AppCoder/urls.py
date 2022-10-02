from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio, name = "Inicio"),
    path("formSerie", formuSerie, name = "FormSerie"),
    path("formPeli", formuPeli, name = "FormPeli"),
    path("formUsuario", formu, name = "FormUsuario"),
    path("buscar", buscarUsuario, name = "Buscador"),
    path("resultados/", busqueda, name = "Resultado"),
    path("cartelera", cartel, name = "cartelera"),

    #CRUD
    path("leerpubli/", leerPub, name="publicaleer"),
    path("crearpubli/", leerPub, name="publicacrear"),
    path("eliminarpubli/<pubTitu>", eliminarPub, name="publicaeliminar"),
    path("editarpubli/<pubTitu>", editarPub, name="publicaeditar")
    
]