
from django.contrib import admin
from django.urls import path,include
from api.views import  *
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.conf.urls  import handler404,handler500

handler404=page_not_found

app_name = 'api'
urlpatterns = [
    path('admin/',admin.site.urls),
    path('',logear,name='login'),
    path('log_out/',log_out,name='log_out'),
    path('api/',include('api.urls')),

    path('registrar/',perfilUsuarioRegistro.as_view(),name='registrar'),
    path('estruc/',perfiluser,name='estruc')
]


