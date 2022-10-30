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
 path('gestor-eliinar-ajax/',ajax_eliminar,name='ajaxeliminar'),
 path('gestor-editar/<int:id>',editarCrudGestor,name='editarGestor'),
 path('gestorRegristocaso',registrarCasoGestor,name='registrarCasoGestor'),
 path('infoComplementaria/',informacionComplementarias,name='info'),
 path('seguimientoGestor/',seguimientoGestor,name='seguimientoGestor'),
 path('infoeditar/<int:id>',editarInfo,name='editarInfo'),
path('seguimientoeditar/<int:id>',editarSegui,name='editarsegui'),
path('actividades/',calendario_activdades,name='actividades'),
path('mostraractividad/<int:id>',mostrarinfo,name='mostraractividad'),
path('guardaractividad/',guardar,name='guardaractividad'),
path('editaractividad/<int:id>',editaractividad,name='editaractividad'),
path('eliminaractividad/<int:id>',actividadCrudDelete,name='eliminaractividad'),
path('ajax_eliminaractividad/',ajax_eliminaractividad,name='ajax_eliminaractividad'),
path('infocreareditar/',informacionComplementariasCrear,name='infocreareditar'),
path('seguicreareditar/',seguimientoGestor_creareditar,name='seguicreareditar'),
path('enviarajaxinfo/',info_co_post_ajax,name='infoajax'),
path('enviarajaxsegui/',segui_co_post_ajax,name='seguioajax'),
path('enviarcorreos/',correo,name='correo')
]
