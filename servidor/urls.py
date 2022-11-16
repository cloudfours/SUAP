

from django.contrib import admin
from django.urls import path,include,re_path
from api.views import  *
from django.views.static import serve
from django.contrib.auth.views import LoginView,PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.decorators import login_required
from django.conf.urls  import handler404,handler500
from django.conf.urls.static import static
from servidor import settings

handler404=page_not_found
handler500=page_error
app_name = 'api'
urlpatterns = [
    path('admin/',admin.site.urls,name='administrador'),
    path('usuario/',logear,name='login'),
    path('log_out/',log_out,name='log_out'),
    path('api/',include('api.urls')),

    path('registrar/',perfilUsuarioRegistro.as_view(),name='registrar'),
    path('estruc/',perfiluser,name='estruc'),
    path('',entrada,name='entrada'),
    path('reset/password_reset/',PasswordResetView.as_view(template_name='RecuperarContraseña/formrecuppss.html',email_template_name='RecuperaRContraseña/correoenviado.html'),name='password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='RecuperarContraseña/enviocorreo.html'), name = 'password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='RecuperarContraseña/resetearcontrasena.html'), name = 'password_reset_confirm'),
    path('reset/done',PasswordResetCompleteView.as_view(template_name='RecuperarContraseña/cofirmar.html') , name = 'password_reset_complete'),
]


urlpatterns += [
    re_path(r'^media/(?P<path>.*)$',serve,{
        'document_root':settings.MEDIA_ROOT,
    })
]
