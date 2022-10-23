from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name = "Inicio"),
    path("buscar", buscarUsuario, name = "Buscador"),
    path("resultados/", busqueda, name = "Resultado"),
    path("login", iniciar, name = "inicio"),
    path("registro", registro, name = "registrando"),
    path("logout", LogoutView.as_view(template_name="AppCoder/inicio.html"), name = "salir"),
    path("editarUser", editarUsuario, name = "editUser"),
    path("agregarAvatar/", agregarAvatar, name="AgregarAvatar"),
    path("perfil/", perfil, name = "Perfil"),
    path('detallePost/<int:pk>/', detallePost.as_view(), name='detallePost'),
    path('detallePost/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    #path('comentario/', comentar, name='comentario'),
    path('about/', about, name='About'),
    path('misPosteos/', misPosteos, name='misPosteos'),
    
    #CRUD
    path("posteo/", posts, name = "Posteos"),
    path("postear/", postear, name = "Postear"),
    path("editarPost/<Posteo>", editarPost, name = "editarPost"),
    path("eliminarPost/<Posteo>", eliminarPost, name = "eliminarPost"),
    
]