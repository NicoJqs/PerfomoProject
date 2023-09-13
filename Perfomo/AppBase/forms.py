from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from AppBase.models import Perfume, Mensaje, Profile

class RegistroUsuarioForm(UserCreationForm):

    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="contrasena", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contrasena", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    email= forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name= forms.CharField(label='Modificar Nombre')
    last_name= forms.CharField(label='Modificar Apellido')
    link_profile = forms.CharField(label='Social Link')
    
    class Meta:
        model=User
        fields=["email", "password1", "password2", "first_name", "last_name", "link_profile"]
        help_texts = {k:"" for k in fields}


class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")


class PerfumeForms(forms.ModelForm):

    class Meta:
        model = Perfume
        fields = ['marca', 'modelo', 'tipo', 'descripcion', 'year','imagenPerfume']
        labels = {
            'marca': 'Marca',
            'modelo': 'Modelo',
            'tipo': 'Tipo',
            'descripcion': 'Descripción',
            'year': 'Year',
            'imagenPerfume': 'Imagen del Perfume',
        }
        help_texts = {k: "" for k in fields}


class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['receiver', 'content']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['linkedin_url', 'github_url']
        widgets = {
            'linkedin_url': forms.URLInput(attrs={'placeholder': 'https://www.linkedin.com/in/tu_usuario'}),
            'github_url': forms.URLInput(attrs={'placeholder': 'https://github.com/tu_usuario'}),
        }