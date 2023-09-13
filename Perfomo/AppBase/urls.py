from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

from .import views

urlpatterns = [
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(next_page=login_request), name="logout"),
    path('register/', register, name="register"),

    path('profile/editarPerfil/', editarPerfil, name="editarPerfil"),
    path('profile/agregarAvatar/', agregarAvatar, name="agregarAvatar"),
    path('profile/editarLink/', edit_profile, name="editarLink"),
    path('profile/verPerfil/', views.view_profile, name="verPerfil"),

    path('perfume/crearPublicacion/', crear_publicacion, name="crearPublicacion"),
    path('perfume/editarPublicacion/<pk>', PerfumeUpdate.as_view(), name="perfume_editar"),
    path('perfume/listPubliciones/', PerfumeList.as_view(), name="listPublicaciones"),
    path('perfume/borrarPublicacion/<pk>', PerfumeDelete.as_view(), name="perfume_borrar"),
    path('perfume/detallePublicacion/<pk>', PerfumeDetalle.as_view(), name="perfume_detalle"),

    path('aboutMe/', about, name='aboutMe'),

    path('enviarMensaje/', enviarMensaje, name='enviarMensaje'),
    path('inbox/', views.inbox, name='inbox'),
    
]