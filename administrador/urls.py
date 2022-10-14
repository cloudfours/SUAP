from django.urls import path,include
from .views import *
from django.contrib.auth.decorators import login_required
urlpatterns = [
 path('administrar/',administrative,name='administrativo'),
]
