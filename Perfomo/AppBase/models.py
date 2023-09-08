from django.db import models
from django.contrib.auth.models import User

    
class Perfume(models.Model):
    usuario=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    marca=models.CharField(max_length=50)
    modelo=models.CharField(max_length=50) 
    tipo=models.CharField(max_length=50) 
    descripcion=models.TextField(max_length=144, null=True, blank=True) 
    year=models.IntegerField()
    precio=models.DecimalField(max_digits=6, decimal_places=2)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    contactoCelular = models.IntegerField()
    contactoEmail = models.EmailField()
    imagenPerfume = models.ImageField(upload_to="media/")

    def __str__(self):
        return f"{self.usuario} - {self.marca} {self.modelo} {self.tipo}"

class Comentario(models.Model):
    perfume = models.ForeignKey(Perfume, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=50)
    mensaje = models.TextField(null=True, blank=True)
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_comentario']

    def __str__(self):
        return f"{self.nombre} - {self.perfume}"

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatars",null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)