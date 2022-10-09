from django.urls import path,include
from .views import *
from django.contrib.auth.decorators import login_required
urlpatterns = [
 path('listMostrarInfo/',perfilUsuario,name='perfil'),
 path('registrarCaso/',registrarCaso,name='caso'),
 path('editarUsuario/<int:id>',editarUser,name='editarUsuario'),
 path('seguimiento/',seguimiento,name='seguimiento')
]
