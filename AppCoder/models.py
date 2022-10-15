from email.policy import default
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Peli(models.Model):
    def __str__(self):
        return f"Título: {self.titulo} ---- Género: {self.genero} ---- Año: {self.anio}"
    titulo = models.CharField(max_length=60)
    genero = models.CharField(max_length=60)
    anio = models.IntegerField()

class Publi(models.Model):
    def __str__(self):
        return f"Título: {self.titulo} ---- Género: {self.genero} ---- Año: {self.anio}"
    titulo = models.CharField(max_length=60)
    genero = models.CharField(max_length=60)
    anio = models.IntegerField()

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", default='blank-profile-picture.png', null=True, blank=True)

    class Meta:
        verbose_name = "Avatar"
        verbose_name_plural = "Avatares"

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='blank-profile-picture.png')

    def __str__(self):
        return f'Perfil de {self.user.username}'

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    imagen = models.ImageField(upload_to="publicaciones", null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    titulo = models.CharField(max_length=60,null=True, blank=True)
    genero = models.CharField(max_length=60,null=True, blank=True)
    anio = models.IntegerField(null=True, blank=True)
    content = models.TextField()
    class Meta:
        ordering = ["-timestamp"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    def __str__(self):
        return f'{self.user.username}: {self.titulo}: {self.genero}'
