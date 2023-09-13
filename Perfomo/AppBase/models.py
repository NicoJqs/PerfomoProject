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


class Mensaje(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} : {self.receiver} - {self.content}"

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username