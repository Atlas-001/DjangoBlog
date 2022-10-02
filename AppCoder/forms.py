from tkinter.ttk import Style
from django import forms

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