from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

from .import views

urlpatterns = [
    path('login/', login_request, name="login"),
    path('register/', register, name="register"),
    path('editarPerfil,', editarPerfil, name="editarPerfil"),
    path('logout/', LogoutView.as_view(next_page=login_request), name="logout"),

    #path('crearPublicacion/', Perfume, name="crearPublicacion"),
    path('crearPublicacion/', crear_publicacion, name="crearPublicacion"),
]