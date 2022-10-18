
import math
import random

from api.models import *
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from .forms import datosuserForm, userRegister, datosuserFormEdit, CasosForm,EditarFormGestor
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

global usuario


@login_required
def perfilUsuario(request):
    usuario = DatosUsuario.objects.filter(
        login_id=request.user.id).select_related('login_id')
    if request.method == 'GET':
        usuario = DatosUsuario.objects.filter(
            login_id=request.user.id).select_related('login_id')

    return render(request, 'informacion_paciente.html', {'usuario': usuario})


@login_required
def editarUser(request, id):
    try:
        persona = DatosUsuario.objects.get(pk=id)
        if request.method == 'GET':
            persona_form = datosuserFormEdit(instance=persona)
        else:
            persona_form = datosuserFormEdit(request.POST, instance=persona)

            if persona_form.is_valid():
                persona_form.save()
                return redirect('perfil')
            else:
                messages.add_message(
                    request, messages.ERROR, message='Vuelva a intetarlo')
    except Exception as e:
        print(e)

    return render(request, 'editarUser.html', {'persona_form': persona_form, 'persona': persona})


class perfilUsuarioRegistro(CreateView):
    model = DatosUsuario
    template_name = 'registro.html'
    form_class = datosuserForm
    second_form_class = userRegister
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super(perfilUsuarioRegistro, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
            return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.login_id = form2.save()
            solicitud.save()
            messages.add_message(request, messages.SUCESS,
                                 message='Registro exitoso')
            
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.add_message(request, messages.ERROR,
                                 message='registro fallido vuelva e intentelo')
            return redirect('login')


def validar_grupo(user):
    return user.groups.filter(name__in=['Analista', 'Gestor', 'Paciente']).exists()


def logear(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(username)

        if not user:
            messages.add_message(request, messages.ERROR,
                                 message='contraseña errada o usuario errado')
            return render(request, 'usuarioPorcorreo.html')

        else:
            if validar_grupo(user):
                login(request, user)
                return redirect('perfil')
            else:
                messages.add_message(request, messages.ERROR,
                                     message='El usuario estara activado pronto')
            return redirect('login')

    return render(request, 'usuarioPorcorreo.html')


def log_out(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, f'ha vuelto al inicio')
    return redirect(reverse('login'))


def perfiluser(request):
    return render(request, 'estructuraSuap.html')


@login_required
def registrarCaso(request):
    datos_usuario =  DatosUsuario.objects.get(login_id=request.user.id)
    caso = Casos.objects.filter(id_usuario = datos_usuario.id_cedula).select_related('estado').filter(estado__idestado=Case(When(estado__nombreestado='abierto',then=Value(1)),When(estado__nombreestado='proceso',then=Value(2)))).count()
    print(caso)
    numeroradicado = math.floor(random.random()* 1000)
    forma_persona = CasosForm(request.POST, request.FILES)
    if request.method == 'POST':
        if caso>=1:
               messages.add_message(request, messages.ERROR,message='No puede crear otro caso hasta que este finalice')
               return redirect('caso') 
        else:
            if forma_persona.is_valid():
                forma_persona.save()
                return redirect('perfil')
    else:
            initial_data = {'id_usuario':datos_usuario.id_cedula,'estado':1,'fecharesgistrocaso':datetime.datetime.now(),'numeroradicado':numeroradicado}
            forma_persona = CasosForm(initial=initial_data)
    return render(request, 'registrarCaso.html', {'forma_persona': forma_persona})


def page_not_found(request,exception):
    return render(request, '404.html')
    
def page(request,exception):
    return render(request,'505.html')
@login_required
def seguimiento(request):
    datos_usuario=DatosUsuario.objects.get(login_id=request.user.id)

    
    casos=Casos.objects.filter(id_usuario= datos_usuario.id_cedula).last()
    
   
    return render(request,'seguimiento.html',{'casos':casos})
@login_required
def historial_casos(request):
    datos_usuario=DatosUsuario.objects.get(login_id=request.user.id)
    
    try:
        casoshistorial = Casos.objects.filter(id_usuario=datos_usuario.id_cedula)
       
        fechafinal = Casos.objects.values('id_caso','fechaatenfinalizado','fecharesgistrocaso').filter(id_usuario= datos_usuario.id_cedula).annotate(duration=F('fechaatenfinalizado') - F('fecharesgistrocaso'))        
    except Casos.DoesNotExist:
        messages.add_message(request,messages.ERROR,message='No existe a un caso creado')

    return render(request,'historial.html',{'casoshistorial': casoshistorial,'dic_fecha':fechafinal})
@login_required
def gestorcrud(request):
    casos = Casos.objects.all()
  
    return render(request,'Gestor/gestorcrud.html',{'casos':casos})

@login_required
def gestorCrudDelete(request,id):
    casos = Casos.objects.all()
   
    if  Casos.objects.filter(pk=id).update(estado_pendiente=False):
        #  messages.add_messages(request,messages.WARNING,message='¿Esta seguro de eliminar?')
         return redirect('busqueda')   
 

    return render(request,'Gestor/advertencia.html',{'casos':casos})

@login_required
def editarCrudGestor(request,id):
   try:
        caso=Casos.objects.get(pk=id)
        if request.method == 'GET':
                forma_persona = EditarFormGestor(instance=caso)
        else:
                forma_persona = EditarFormGestor(request.POST,request.FILES,instance=caso)
                
                # files=request.FILES.getlist('formula_medica')
                if forma_persona.is_valid(): 
                    forma_persona.save()
                    return redirect('busqueda')
                else:
                   messages.add_message(request, messages.ERROR, message='LLENE LOS CAMPOS FALTANTES')
   except AttributeError as e:
                    print(e)
               
     
   return render(request,'Gestor/editarCasoGestor.html',{'forma_persona':forma_persona,'caso':caso})


#  try:
#         persona = DatosUsuario.objects.get(pk=id)
#         if request.method == 'GET':
#             persona_form = datosuserFormEdit(instance=persona)
#         else:
#             persona_form = datosuserFormEdit(request.POST, instance=persona)

#             if persona_form.is_valid():
#                 persona_form.save()
#                 return redirect('perfil')
#             else:
#                 messages.add_message(
#                     request, messages.ERROR, message='Vuelva a intetarlo')
#     except Exceptio