from django import forms

class Formulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    mail = forms.EmailField()

class PeliForm(forms.Form):
    titulo = forms.CharField()
    genero = forms.CharField()
    anio = forms.IntegerField()