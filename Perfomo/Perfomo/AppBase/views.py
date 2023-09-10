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
from .models import Perfume, Avatar, Perfume
from .forms import RegistroUsuarioForm, UserEditForm, AvatarForm, PerfumeForms

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
            return render(request, "AppBase/inicio.html", {"mensaje": f"The Username {nombre_usuario} has been created successfully."})
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
                return render(request, "AppBase/inicio.html", {"mensaje":f"The username {usu} has been successfully logged in."})
            else:
                return render(request, "AppBase/login.html", {"form":form, "mensaje":"Datos invalidos (1)"})
        else:
            return render(request, "AppBase/login.html", {"form":form, "mensaje":"The username or password is not correct. Try again."})
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
            perfume = form.save(commit=False)
            if form.cleaned_data['year']:
                perfume.usuario = request.user
                perfume.save()
                return render(request, "AppBase/inicio.html", {"mensaje":"Publicacion creada Correctamente"})
            else:
                form.add_error('year', 'El campo "Año de creación" es obligatorio.')
        else:
            return render(request, "AppBase/crearPublicacion.html", {"mensaje": "Error, no se pudo generar la publicacion."})
    else:
        form = PerfumeForms()    
        
    return render(request, "AppBase/crearPublicacion.html", {'form': form})

@login_required
def editarPublicacion(request, id):
    perfume = Perfume.objects.get(id = id)
    if request.method == 'POST':
        form = PerfumeForms(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            perfume.marca = info["marca"]
            perfume.modelo = info["modelo"]
            perfume.tipo = info["tipo"]
            perfume.descripcion = info["descripcion"]
            perfume.year = info["year"]
            perfume.imagenPerfume = info["imagenPerfume"]
            perfume.save()

            mensaje = "Publicacion editada."
            perfumes = Perfume.objects.all()
            form_perfume = PerfumeForms()
            return render(request, "AppBase/inicio.html", {"mensaje":mensaje, "form": form_perfume})
    else:
        form_perfume = PerfumeForms( initial={"marca": perfume.marca, "modelo": perfume.modelo, "tipo": perfume.tipo, "descripcion": perfume.descripcion, "year": perfume.year, "imagenPerfume": perfume.imagenPerfume})
        return render(request, "AppBase/editarPublicacion.html", {"form": form_perfume, "perfume": perfume})
    
    
class PerfumeList(ListView):
    model = Perfume
    template_name = "AppBase/listPublicaciones.html"

class PerfumeUpdate(LoginRequiredMixin, UpdateView):
    model = Perfume
    template_name = "AppBase/perfume_editar.html"
    success_url = reverse_lazy("listPublicaciones")
    fields = ['marca', 'modelo', 'tipo', 'descripcion', 'year', 'imagenPerfume']

class PerfumeDelete(LoginRequiredMixin, DeleteView):
    model = Perfume
    success_url = reverse_lazy("listPublicaciones")

class PerfumeDetalle(DetailView):
    model = Perfume
    template_name = "AppBase/perfume_detalle.html"

def about(request):
    return render(request, "AppBase/aboutMe.html",)

def verPerfil(reqeust):
    pass
