from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()

class Peli(models.Model):
    titulo = models.CharField(max_length=60)
    genero = models.CharField(max_length=60)
    anio = models.IntegerField()