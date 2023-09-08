from django.shortcuts import render, redirect

from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from django import forms
from .models import Perfume, Comentario, Avatar, Perfume
from .forms import RegistroUsuarioForm, UserEditForm, AvatarForm, PerfumeForms

@login_required
def obtenerAvatar(request):

    avatares=Avatar.objects.filter(user=request.user.id)
    
    if len(avatares)!=0:
        
        return avatares[0].imagen.url
    else:
        return "/media/avatars/avatarpordefecto.png"
    

def inicio(request):
    avatar= obtenerAvatar(request)   
    return render(request,"AppBase/inicio.html", {"avatar":obtenerAvatar(request)})



def register(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre_usuario=info["username"]
            form.save()
            return render(request, "AppBase/inicio.html", {"mensaje":f"Usuario {nombre_usuario} creado correctamente"})
        else:
            return render(request,"AppBase/register.html", {"form":form, "mensaje":"Datos invalidos"})

    else:
        form=RegistroUsuarioForm()
        return render(request,"AppBase/register.html", {"form":form})
    

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppBase/inicio.html", {"mensaje":f"Usuario {usu} logueado correctamente"})
            else:
                return render(request, "AppBase/login.html", {"form":form, "mensaje":"Datos invalidos (1)"})
        else:
            return render(request, "AppBase/login.html", {"form":form, "mensaje":"Datos invalidos (2)"})
    else:
        form=AuthenticationForm()
        return render(request, "AppBase/login.html", {"form":form})

@login_required
def editarPerfil(request):
    avatar= obtenerAvatar(request) 
    usuario=request.user

    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():

            info=form.cleaned_data

            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()

            return render(request, "AppBase/inicio.html", {"avatar":avatar,"mensaje":f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "AppBase/editarPerfil.html", {"form": form, "avatar":avatar,"nombreusuario":usuario.username, "mensaje":"Datos invalidos"})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "AppBase/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})

@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "AppBase/inicio.html", {"mensaje":f"Avatar agregado correctamente", "avatar":obtenerAvatar(request)})
        else:
            return render(request, "AppBase/agregarAvatar.html", {"form": form, "usuario": request.user, "mensaje":"Error al agregar el avatar"})
    else:
        form=AvatarForm()
        return render(request, "AppBase/agregarAvatar.html", {"form": form, "usuario": request.user, "avatar":obtenerAvatar(request)})

@login_required
def crear_publicacion(request):
    if request.method == 'POST':
        form = PerfumeForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "AppBase/inicio.html", {"mensaje":"Publicacion creada Correctamente"})
    else:
        form = PerfumeForms()
    
    return render(request, "AppBase/crearPublicacion.html", {'form': form})
