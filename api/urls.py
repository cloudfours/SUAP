from django.urls import path,include
from .views import *
from django.contrib.auth.decorators import login_required
urlpatterns = [
 path('listMostrarInfo/',perfilUsuario,name='perfil'),
 path('registrarCaso/<int:id>',registrarCaso,name='caso'),
 path('editarUsuario/<int:id>',editarUser,name='editarUsuario'),
 path('registrarCaso/',registrarCaso,name='caso'),
 path('editarUsuario/<int:id>',editarUser,name='editarUsuario'),
 path('seguimiento/',seguimiento,name='seguimiento'),
 path('historial',historial_casos,name='historial'),
 path('gestorbusqueda/',gestorcrud,name='busqueda'),
 path('gestorbusqueda-eliminar/<int:id>',gestorCrudDelete,name='eliminar'),

]
