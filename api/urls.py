from django.urls import path,include

from servidor import settings
from .views import *
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
urlpatterns = [
 path('listMostrarInfo/',perfilUsuario,name='perfil'),
 path('editarUsuario/<int:id>',editarUser,name='editarUsuario'),
 path('registrarCaso/',registrarCaso,name='caso'),
 path('seguimiento/',seguimiento,name='seguimiento'),
 path('historial',historial_casos,name='historial'),
 path('gestorbusqueda/',gestorcrud,name='busqueda'),
 path('gestor-eliminar/<int:id>',gestorCrudDelete,name='eliminar'),
 path('gestor-editar/<int:id>',editarCrudGestor,name='editarGestor'),
 path('gestorRegristocaso',registrarCasoGestor,name='registrarCasoGestor'),

]
