from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def vista(request):
    return render(request, "AppCoder/vista.html")