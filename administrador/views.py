
from api.models import *
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from api.forms import datosuserForm, userRegister, datosuserFormEdit, CasosForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView
from django.db.models import When,Case,Value,F,Count
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import datetime
from django.core.exceptions import ObjectDoesNotExist

@login_required
def administrative(request):
    return render(request,'administrador/administrador.html')
