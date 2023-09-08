from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from AppBase.models import Perfume

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}

class UserEditForm(UserChangeForm):
    email = forms.EmailField(label="Email Usuario")

    class Meta:
        model = User
        fields = ["email", "password"]

class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="Imagen")

class PerfumeForms(forms.ModelForm):
    class Meta:
        model = Perfume
        fields = ['marca', 'modelo', 'tipo', 'descripcion', 'year', 'precio', 'contactoCelular', 'contactoEmail', 'imagenPerfume']
        labels = {
            'marca': 'Marca',
            'modelo': 'Modelo',
            'tipo': 'Tipo',
            'descripcion': 'Descripción',
            'year': 'Año de creación',
            'precio': 'Precio',
            'contactoCelular': 'Número de Contacto',
            'contactoEmail': 'Correo Electrónico',
            'imagenPerfume': 'Imagen del Perfume',
        }
        help_texts = {k: "" for k in fields}