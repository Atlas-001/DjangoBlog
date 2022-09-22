from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Usuario
from .forms import Formulario
def inicio(request):
    return render(request, "AppCoder/inicio.html")

def vista(request):
    return render(request, "AppCoder/vista.html")

def formu(request):
    if request.method == "POST":
        formulario1 = Formulario(request.POST)
        if formulario1.is_valid():
            info = formulario1.cleaned_data
            usuarioF = Usuario(nombre = info["nombre"], apellido = info["apellido"], correo = info["mail"])
            usuarioF.save()
            return render(request, "AppCoder/formulario.html")
    else:
        formulario1 = Formulario()
    return render(request, "AppCoder/formulario.html", {"form1":formulario1})

def buscarUsuario(request):
    return render(request, "AppCoder/buscandoUsuario.html")

def busqueda(request):
    if request.GET["nombre"]:
        buscar = request.GET["nombre"]
        usuario = Usuario.objects.filter(nombre_icontains=buscar)
        return render(request, "AppCoder/resultados.html", {"usuario":usuario, "buscar":buscar})
    else:
        mensaje = "No enviaste datos."
    return HttpResponse(mensaje)
