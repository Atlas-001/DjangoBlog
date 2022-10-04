from dataclasses import fields
import email
from tkinter.ttk import Style
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Formulario(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Nombre"}), label="")
    apellido = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Apellido"}), label="")
    mail = forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"Correo"}), label="")

class PeliForm(forms.Form):
    titulo = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Título"}), label="")
    genero = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Genero"}), label="")
    anio = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":"Año"}), label="")

class SerieForm(forms.Form):
    titulo = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Título"}), label="")
    genero = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Genero"}), label="")
    anio = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":"Año"}), label="")

class PubliForm(forms.Form):
    titulo = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Título"}), label="")
    genero = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Genero"}), label="")
    anio = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":"Año"}), label="")

class RegistroForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"Ingrese un correo"}), label="")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Ingrese una contraseña"}), label="")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Repita la contraseña"}), label="")
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

class EditarUsuarioForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"Ingrese un correo"}), label="")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Ingrese una contraseña"}), label="")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Repita la contraseña"}), label="")
    class Meta:
        model = User
        fields = ["email","password1","password2"]
        
