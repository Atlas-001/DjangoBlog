from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name = "Inicio"),
    path("formPeli", formuPeli, name = "FormPeli"),
    path("buscar", buscarUsuario, name = "Buscador"),
    path("resultados/", busqueda, name = "Resultado"),
    path("cartelera", cartel, name = "cartelera"),
    path("login", iniciar, name = "inicio"),
    path("registro", registro, name = "registrando"),
    path("logout", LogoutView.as_view(template_name="AppCoder/inicio.html"), name = "salir"),
    path("editarUser", editarUsuario, name = "editUser"),
    path("agregarAvatar/", agregarAvatar, name="AgregarAvatar"),
    path("perfil/", perfil, name = "Perfil"),
    path("posteo/", posts, name = "Posteos"),
    path("postear/", postear, name = "Postear"),
    path("editarPost/<Posteo>", editarPost, name = "editarPost"),
    path("eliminarPost/<Posteo>", eliminarPost, name = "eliminarPost"),
    path('detallePost/<int:pk>/', detallePost.as_view(), name='detallePost'),

    #CRUD
    path("leerpubli/", leerPub, name="publicaleer"),
    path("crearpubli/", crearPub, name="publicacrear"),
    path("eliminarpubli/<pubTitu>", eliminarPub, name="publicaeliminar"),
    path("editarpubli/<pubTitu>", editarPub, name="publicaeditar"),
    
]