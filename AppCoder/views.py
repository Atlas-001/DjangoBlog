from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def formu(request):
    if request.method == "POST":
        formulario1 = Formulario(request.POST)
        if formulario1.is_valid():
            info = formulario1.cleaned_data
            usuarioF = Usuario(nombre = info["nombre"], apellido = info["apellido"], correo = info["mail"])
            usuarioF.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario1 = Formulario()
    return render(request, "AppCoder/formulario.html", {"form1":formulario1})

def formuPeli(request):
    if request.method == "POST":
        formulario2 = PeliForm(request.POST)
        if formulario2.is_valid():
            info = formulario2.cleaned_data
            peliF = Peli(titulo = info["titulo"], genero = info["genero"], anio = info["anio"])
            peliF.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario2 = PeliForm()
    return render(request, "AppCoder/peliform.html", {"form2":formulario2})

def formuSerie(request):
    if request.method == "POST":
        formulario3 = SerieForm(request.POST)
        if formulario3.is_valid():
            info = formulario3.cleaned_data
            serieF = Serie(titulo = info["titulo"], genero = info["genero"], anio = info["anio"])
            serieF.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario3 = SerieForm()
    return render(request, "AppCoder/serieform.html", {"form3":formulario3})

def buscarUsuario(request):
    return render(request, "AppCoder/buscando.html")

def busqueda(request):
    if request.GET["titulo"]:
        buscar = request.GET["titulo"]
        pelis = Peli.objects.filter(titulo__icontains=buscar)
        return render(request, "AppCoder/resultados.html", {"pelis":pelis, "buscar":buscar})
    else:
        mensaje = "No enviaste datos."
    return HttpResponse(mensaje)



def cartel(request):
    listadoPeli = Peli.objects.all()
    return render(request, "AppCoder/cartelera.html",{"titulo":listadoPeli})

def leerPub(request):
    publi = Peli.objects.all()
    contexto = {"publi":publi}
    return render(request, "AppCoder/leerPubli.html", contexto)

def crearPub(request):
    if request.method == "POST":
        crearPublicacion = PubliForm(request.POST)
        if crearPublicacion.is_valid():
            info = crearPublicacion.cleaned_data
            publi = Publi(titulo = info["titulo"], genero = info["genero"], anio = info["anio"])
            publi.save()
            return render(request, "AppCoder/inicio.html")
    else:
        crearPublicacion = PubliForm()
    return render(request, "AppCoder/publiform.html", {"publicar":crearPublicacion})

def eliminarPub(request, pubTitu):
    titu = Publi.objects.get(titulo = pubTitu)
    titu.delete()
    titulos = Publi.objects.all()
    contexto = {"titulos":titulos}
    return render(request, "AppCoder/leerPubli.html", contexto)

def editarPub(request, pubTitu):
    pubt = Publi.objects.get(titulo = pubTitu)
    if request.method == "POST":
        crearPublicacion = PubliForm(request.POST)
        if crearPublicacion.is_valid():
            info = crearPublicacion.cleaned_data
            pubt.titulo = info["titulo"]
            pubt.genero = info["genero"]
            pubt.anio = info["anio"]
            pubt.save()
            return render(request, "AppCoder/inicio.html")
    else:
        crearPublicacion = PubliForm(initial={"titulo": pubt.titulo, "genero": pubt.genero, "anio": pubt.anio})
    return render(request, "AppCoder/editarPubli.html", {"publicar":crearPublicacion, "nombre":pubTitu})