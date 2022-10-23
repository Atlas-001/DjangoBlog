from email.policy import default
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", default='', null=True, blank=True)

    class Meta:
        verbose_name = "Avatar"
        verbose_name_plural = "Avatares"

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(default='', null=True, blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    imagen = models.ImageField(upload_to="publicaciones", null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    titulo = models.CharField(max_length=60,null=True, blank=True)
    genero = models.CharField(max_length=60,null=True, blank=True)
    anio = models.IntegerField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    class Meta:
        ordering = ["-timestamp"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    def __str__(self):
        return f'{self.user.username}: {self.titulo}: {self.genero}'

class Comentar(models.Model):
    comentario = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios', null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario', null=True)
    imagen = models.ImageField(default='', null=True, blank=True)
    timecoment = models.DateTimeField(default=timezone.now)
    mensaje = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-timecoment']
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return f'{self.user.username}'
