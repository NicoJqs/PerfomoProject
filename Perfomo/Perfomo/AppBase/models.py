from django.db import models
from django.contrib.auth.models import User

    
class Perfume(models.Model):
    usuario=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    marca=models.CharField(max_length=50)
    modelo=models.CharField(max_length=50) 
    tipo=models.CharField(max_length=50) 
    descripcion=models.TextField(null=True, blank=True)
    year = models.IntegerField()
    imagenPerfume = models.ImageField(upload_to="media/")

    def __str__(self):
        return f"{self.usuario} - {self.marca} {self.modelo} {self.tipo}"

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatars",null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)