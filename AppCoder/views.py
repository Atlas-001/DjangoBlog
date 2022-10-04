from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, "AppCoder/inicio.html")

@login_required#(login_url='inicio')
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

@login_required
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

@login_required
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

@login_required
def buscarUsuario(request):
    return render(request, "AppCoder/buscando.html")

@login_required
def busqueda(request):
    if request.GET["titulo"]:
        buscar = request.GET["titulo"]
        pelis = Peli.objects.filter(titulo__icontains=buscar)
        return render(request, "AppCoder/resultados.html", {"pelis":pelis, "buscar":buscar})
    else:
        mensaje = "No enviaste datos."
    return HttpResponse(mensaje)


@login_required
def cartel(request):
    listadoPeli = Peli.objects.all()
    return render(request, "AppCoder/cartelera.html",{"titulo":listadoPeli})

@login_required
def leerPub(request):
    publi = Publi.objects.all()
    contexto = {"publi":publi}
    return render(request, "AppCoder/leerPubli.html", contexto)

@login_required
def crearPub(request):
    if request.method == "POST":
        crearPublicacion = PubliForm(request.POST)
        if crearPublicacion.is_valid():
            info = crearPublicacion.cleaned_data
            publi = Publi(titulo = info["titulo"], genero = info["genero"], anio = info["anio"])
            publi.save()
            return render(request, "AppCoder/leerPubli.html")
    else:
        crearPublicacion = PubliForm()
    return render(request, "AppCoder/publiform.html", {"publicar":crearPublicacion})

@login_required
def eliminarPub(request, pubTitu):
    titu = Publi.objects.get(titulo = pubTitu)
    titu.delete()
    titulos = Publi.objects.all()
    contexto = {"titulos":titulos}
    return render(request, "AppCoder/leerPubli.html", contexto)

@login_required
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
            return render(request, "AppCoder/leerPubli.html")
    else:
        crearPublicacion = PubliForm(initial={"titulo": pubt.titulo, "genero": pubt.genero, "anio": pubt.anio})
    return render(request, "AppCoder/editarPubli.html", {"publicar":crearPublicacion, "nombre":pubTitu})

def iniciar(request):
    if request.method == "POST":
        ingresar = AuthenticationForm(request, data = request.POST)
        if ingresar.is_valid():
            usuario = ingresar.cleaned_data.get("username")
            contra = ingresar.cleaned_data.get("password")
            user = authenticate(username = usuario, password = contra)
            if user:
                login(request, user)
                return render(request, "AppCoder/inicio.html",{"mensaje":f"hola {user}"})
        else:
            return render(request, "AppCoder/inicio.html",{"mensaje":f"Datos incorrectos"})
    else:
        ingresar = AuthenticationForm()
    return render(request, "AppCoder/login.html",{"ingresar":ingresar})

def registro(request):
    if request.method == "POST":
        registrar = RegistroForm(request.POST)
        if registrar.is_valid():
            nombreUsuario = registrar.cleaned_data["username"]
            registrar.save()
            return render(request, "AppCoder/inicio.html",{"mensaje":f"Usuario {nombreUsuario} creado!!"})
    else:
        registrar = RegistroForm()
    return render(request, "AppCoder/registro.html",{"registrar":registrar})

def editarUsuario(request):
    userConect = request.user
    if request.method == "POST":
        usuarioform = EditarUsuarioForm(request.POST)
        if usuarioform.is_valid():
            info = usuarioform.cleaned_data
            userConect.email = info["email"]
            userConect.password1 = info["password1"]
            userConect.password2 = info["password2"]
            userConect.save()
            return render(request, "AppCoder/inicio.html")
    else:
        usuarioform = EditarUsuarioForm(initial={"email": userConect.email})
    return render(request, "AppCoder/editarUsuario.html", {"userEdit":usuarioform, "userOn":userConect})