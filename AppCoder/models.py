from django.db import models

class Usuario(models.Model):

    def __str__(self):
        return f"Nombre: {self.nombre} ---- Apellido: {self.apellido} ---- Correo: {self.correo}"
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()

class Peli(models.Model):
    def __str__(self):
        return f"Título: {self.titulo} ---- Género: {self.genero} ---- Año: {self.anio}"
    titulo = models.CharField(max_length=60)
    genero = models.CharField(max_length=60)
    anio = models.IntegerField()

class Serie(models.Model):
    def __str__(self):
        return f"Título: {self.titulo} ---- Género: {self.genero} ---- Año: {self.anio}"
    titulo = models.CharField(max_length=60)
    genero = models.CharField(max_length=60)
    anio = models.IntegerField()