from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name = "Inicio"),
    path("formSerie", formuSerie, name = "FormSerie"),
    path("formPeli", formuPeli, name = "FormPeli"),
    path("formUsuario", formu, name = "FormUsuario"),
    path("buscar", buscarUsuario, name = "Buscador"),
    path("resultados/", busqueda, name = "Resultado"),
    path("cartelera", cartel, name = "cartelera"),
    path("login", iniciar, name = "inicio"),
    path("registro", registro, name = "registrando"),
    path("logout", LogoutView.as_view(template_name="AppCoder/inicio.html"), name = "salir"),
    path("editarUser", editarUsuario, name = "editUser"),

    #CRUD
    path("leerpubli/", leerPub, name="publicaleer"),
    path("crearpubli/", crearPub, name="publicacrear"),
    path("eliminarpubli/<pubTitu>", eliminarPub, name="publicaeliminar"),
    path("editarpubli/<pubTitu>", editarPub, name="publicaeditar"),
    
]