from django import forms

class Formulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    mail = forms.EmailField()
