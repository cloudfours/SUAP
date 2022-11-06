
import json
import math
import random
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
import os


from reportlab.pdfgen import canvas
from io import BytesIO

from django.http import HttpResponse
from django.core import serializers
from api.models import *
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from .forms import datosuserForm, userRegister, datosuserFormEdit, CasosForm,EditarFormGestor,informacionComplementaria,seguimientoFormulario,AsignacionTareaForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView
from django.db.models import When,Case,Value,F,Count,Sum
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import datetime
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
global usuario


@login_required
def perfilUsuario(request):
    usuario = DatosUsuario.objects.filter(
        login_id=request.user.id).select_related('login_id')
    if request.method == 'GET':
        usuario = DatosUsuario.objects.filter(
            login_id=request.user.id).select_related('login_id')

    return render(request, 'informacion_paciente.html', {'usuario': usuario})
'''
registro y crud del usuario
'''

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
            messages.add_message(request, messages.SUCCESS,
                                 message='Registro exitoso')
            
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.add_message(request, messages.ERROR,
                                 message='registro fallido vuelva e intentelo')
            return redirect('login')


def validar_grupo(user):
    return user.groups.filter(name__in=['Administrador','Analista', 'Gestor', 'Paciente']).exists()


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
'''
aqui empieza el crud del paciente
'''

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
'''
aqui empieza el crud de los casos
'''

@login_required
def gestorcrud(request):
    casos = Casos.objects.all()
    abierto = Casos.objects.all().filter(estado__idestado=1).count()
    proceso=Casos.objects.all().filter(estado__idestado=2).count()
    finalizado=Casos.objects.all().filter(estado__idestado=3).count()
    modal_status='eliminar'
    return render(request,'Gestor/gestorcrud.html',{'casos':casos,'abierto':abierto,'proceso':proceso,'finalizado':finalizado,'modal_status':modal_status})

@login_required
def gestorCrudDelete(request,id):

    casos=Casos.objects.get(pk=id)
    print(casos)
    return render(request,'Gestor/eliminarcaso.html',{'casos':casos})

@login_required
def ajax_eliminar(request):
    id_caso = request.POST.get('id_caso')

    Casos.objects.filter(id_caso=id_caso).update(estado_pendiente='0')
  
   
    response={}
    return JsonResponse(response)

@login_required
def editarCrudGestor(request,id):
   try:
           
        infocom = InfoComplementaria.objects.all().last()
        segui = Seguimiento.objects.all().last()
        caso=Casos.objects.get(pk=id)
        if request.method == 'GET':
              
                forma_persona = EditarFormGestor(instance=caso)
             
        else:
                forma_persona = EditarFormGestor(request.POST,request.FILES,instance=caso)
               
               
                # files=request.FILES.getlist('formula_medica')
                if forma_persona.is_valid(): 
                    forma_persona.save()
                    messages.add_message(request, messages.SUCCESS, message='Se ha editado con exito')
                    return redirect('busqueda')
                else:
                   initial_data = {'id_seguimiento':segui,'id_comple_info':infocom}
                   forma_persona = CasosForm(initial=initial_data)
   except AttributeError as e:
                   print(e)
               
     
   return render(request,'Gestor/editarCasoGestor.html',{'forma_persona':forma_persona,'caso':caso})

@login_required
def registrarCasoGestor(request):
    # datos_usuario =  DatosUsuario.objects.get(login_id=request.user.id)
  
    
    infocom = InfoComplementaria.objects.all().last()
    segui = Seguimiento.objects.all().last()
    numeroradicado = math.floor(random.random()* 1000)
    forma_persona = EditarFormGestor(request.POST, request.FILES)
    if request.method == 'POST':
            if forma_persona.is_valid():
                forma_persona=forma_persona.save(commit=False)
                caso = Casos.objects.filter(id_usuario = int(request.POST['id_usuario'])).select_related('estado').filter(estado__idestado=Case(When(estado__nombreestado='abierto',then=Value(1)),When(estado__nombreestado='proceso',then=Value(2)))).count()
                if caso>=1:
                    messages.add_message(request, messages.ERROR,message='este usuario que selecciono ya tiene un caso abierto')
                    return redirect('registrarCasoGestor')
                else:
                    forma_persona.save()
                    return redirect('busqueda')
            else:
                messages.add_message(request, messages.ERROR,message='Ingrese informacion complementaria y de seguimiento')
    else:
            initial_data = {'estado':1,'fecharesgistrocaso':datetime.datetime.now(),'numeroradicado':numeroradicado,'id_comple_info':infocom,'id_seguimiento':segui}
            forma_persona = EditarFormGestor(initial=initial_data)
    return render(request, 'Gestor/registroCasoGestor.html', {'forma_persona': forma_persona})


@login_required
def informacionComplementarias(request):

    if request.method == 'POST':
        forma_persona = informacionComplementaria(request.POST)
        
        if forma_persona.is_valid():
            forma_persona = forma_persona.save()
            messages.add_message(request,messages.SUCCESS,message='Se aguardo con exito')
            return redirect('registrarCasoGestor')
        
    else:
        forma_persona=informacionComplementaria()
    return render(request,'Gestor/informacionComplementaria.html',{'forma_persona':forma_persona})
@login_required           
def informacionComplementariasCrear(request):
     

    forma_persona=informacionComplementaria()
    return render(request,'Gestor/informacionComplementariacreareditar.html',{'forma_persona':forma_persona})    
@login_required
def info_co_post_ajax(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
           forma_persona=informacionComplementaria(request.POST)
           if forma_persona.is_valid():
               forma_persona=forma_persona.save()
               serializar=serializers.serialize('json',[forma_persona,])
               return JsonResponse({'exito':serializar},status=200)
           else:
               return JsonResponse({'error':serializar},status=400)
    return JsonResponse({"error": ""}, status=400)
@login_required
def seguimientoGestor(request):
    seguimientoForm=seguimientoFormulario(request.POST) 
    if request.method=='POST':
        seguimientoForm=seguimientoFormulario(request.POST)
        if seguimientoForm.is_valid():
            seguimientoForm= seguimientoForm.save()
            return redirect('registrarCasoGestor')
        else:
            seguimientoForm=seguimientoFormulario()
    return render(request,'Gestor/seguimientoGestor.html',{'seguimientoForm':seguimientoForm})

@login_required
def seguimientoGestor_creareditar(request):
    seguimientoForm=seguimientoFormulario() 
   
    return render(request,'Gestor/seguimientoGestorcreareditar.html',{'seguimientoForm':seguimientoForm})
@login_required
def segui_co_post_ajax(request):

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
           segui_form=seguimientoFormulario(request.POST)

           if segui_form.is_valid():
           
               segui_form=segui_form.save()
               segui=serializers.serialize('json',[segui_form,])
               return JsonResponse({'exito':segui},status=200)
           else:
            
               return JsonResponse({'error':segui},status=400)
    return JsonResponse({"error": ""}, status=400)
@login_required
def editarInfo(request,id):

      try:
        complementaria=InfoComplementaria.objects.get(pk=id)
        if request.method == 'GET':
                forma_persona = informacionComplementaria(instance=complementaria)
        else:
                forma_persona = informacionComplementaria(request.POST,request.FILES,instance=complementaria)
                
                # files=request.FILES.getlist('formula_medica')
                if forma_persona.is_valid(): 
                    forma_persona.save()
                    messages.add_message(request, messages.SUCCESS, message='Se ha editado con exito')
                    return redirect('busqueda')
                else:
                   messages.add_message(request, messages.ERROR, message='LLENE LOS CAMPOS FALTANTES')
      except AttributeError as e:
                   print(e)
               

      return render(request,'Gestor/editarinfoco.html',{'forma_persona':forma_persona,'complementaria':complementaria})
  
@login_required
def editarSegui(request,id):
      try:
        seguimiento=Seguimiento.objects.get(pk=id)
        if request.method == 'GET':
                forma_persona = seguimientoFormulario(instance=seguimiento)
        else:
                forma_persona = seguimientoFormulario(request.POST,request.FILES,instance=seguimiento)
                
                # files=request.FILES.getlist('formula_medica')
                if forma_persona.is_valid(): 
                    forma_persona.save()
                    messages.add_message(request, messages.SUCCESS, message='Se ha editado con exito')
                    return redirect('busqueda')
                else:
                   messages.add_message(request, messages.ERROR, message='LLENE LOS CAMPOS FALTANTES')
      except Exception as e:
                   print(e)
               

      return render(request,'Gestor/editarsegui.html',{'forma_persona':forma_persona,'seguimiento':seguimiento})
'''
aqui empieza el crud de actividades  
'''
  
@login_required
def calendario_activdades(request):
   actividad = AsignacionTarea.objects.all()
   return render(request,'Gestor/datercrud/actividadestareas.html',{'actividad':actividad})

@login_required
def guardar(request):
      actividad = AsignacionTareaForm()
      if request.method == 'POST':
            actividad = AsignacionTareaForm(request.POST)
            if actividad.is_valid():
                actividad = actividad.save()
                return redirect('actividades')
            else:
                 actividad = AsignacionTareaForm()
      return render(request,'Gestor/datercrud/creartarea.html',{'actividad':actividad})

@login_required
def mostrarinfo(request,id):
    mostratinfodetalle=AsignacionTarea.objects.get(pk=id)
   
    return render(request,'Gestor/datercrud/mostrarmodalactividad.html',{'mostratinfodetalle':mostratinfodetalle})

@login_required
def editaractividad(request,id):
    mostratinfodetalle=AsignacionTarea.objects.get(pk=id)
    if request.method=='GET':
        actividad = AsignacionTareaForm(instance=mostratinfodetalle)
    else:
        actividad=AsignacionTareaForm(request.POST,instance=mostratinfodetalle)
        if actividad.is_valid():
            actividad = actividad.save()
            messages.add_message(request, messages.SUCCESS, message='Se ha editado con exito')
            return redirect('actividades')
        else:
              messages.add_message(request, messages.ERROR, message='LLENE LOS CAMPOS FALTANTES')
    return render(request, 'Gestor/datercrud/editaractividadmodal.html',{'actividad':actividad,'mostrarinfodetalle':mostratinfodetalle})
# def obtener_gestor(_request):
#     gestor=AsignacionTarea.objects.all()
#     success =[]
#     for valor in gestor:
#         success.append(valor)

#     print(success)
  
        
#     return JsonResponse(success, safe=False)
    
@login_required
def actividadCrudDelete(request,id):

    asig=AsignacionTarea.objects.get(pk=id)
    print(asig)
    return render(request,'Gestor/datercrud/eliminaractividad.html',{'asig':asig})

@login_required
def ajax_eliminaractividad(request):
    id = request.POST.get('id')

    AsignacionTarea.objects.filter(id=id).update(estado_pendiente='0')
  
   
    response={}
    return JsonResponse(response)

def entrada(request):
    return render(request,'entrada.html')
'''
envios de correos
'''
@login_required
def correo(request):
    print(request.POST)
    if request.method=='POST':
    
        para = request.POST["para"]
        asunto=request.POST.get("asunto")
        mensaje=request.POST["mensaje"]
        
        desde = settings.EMAIL_HOST_USER
        email = EmailMessage(asunto,mensaje,desde,to=[para])
        email.fail_silenty=False
        email.send()  
        uploaded_file = request.FILES
        for file in uploaded_file.getlist('adjunto'):
          
           email.attach_file(file.name, file.read(), file.content_type)
           print('-------------------',file.name)
        email.fail_silenty=False
        email.send()  
        return redirect('busqueda')
    else:
        redirect('correo')
    
    
    return render(request,'Gestor/correo.html')

'''
aqui empieza los reportes
'''

@login_required
def generar_report_caso(_request,id):
  template_name='Gestor/reporte_por_caso.html'
  caso = Casos.objects.get(pk=id)
  data = {
      'caso':caso
  }
  
  return HttpResponse(pdf,content_type='application/pdf')



@login_required
def pagina_report(request):
    return render(request,'Gestor/reporte_por_casol.html')


'''
aqui empieza las graficas 
'''
@login_required
def vista_graficas(request):
    casos=Casos.objects.all()
    proceso=[]
    labelsproceso=[]
    finalizado=[]
    labelsfinalizado=[]
    abierto=[]
    labelsabierto=[]
    estados=[]
    labelsestados=[]
    epss=[]
    labelseps=[]
    reg=[]
    labelsreg=[]
    regcont=[]
    labelsregcont=[]
    sub=[]
    labelssub=[]
    depart=[]
    labelsdep=[]
    muni=[]
    labelsmuni=[]
    generos=[]
    labelsge=[]
    enfer=[]
    labelsenfe=[]
    medic=[]
    labelsmedic=[]
    barr=[]
    labelsbarr=[]
    queryabierto= Casos.objects.values('estado__nombreestado').filter(estado__nombreestado='abierto').annotate(cant_estado=Count('estado'))
    queryproceso= Casos.objects.values('estado__nombreestado').filter(estado__nombreestado='proceso').annotate(cant_estado=Count('estado'))
    queryfinalizado= Casos.objects.values('estado__nombreestado').filter(estado__nombreestado='finalizado').annotate(cant_estado=Count('estado'))
    queryestados=Casos.objects.values('estado__nombreestado').annotate(cant_estado=Count('estado'))
    eps = Casos.objects.values('id_usuario__id_eps__nombre').annotate(cant_eps=Count('id_usuario__id_eps'))
    regimen=Casos.objects.values('id_usuario__idtiporegimen__nombreregimen').annotate(cant_reg=Count('id_usuario__idtiporegimen__nombreregimen'))
    regimencont=Casos.objects.values('id_usuario__idtiporegimen__nombreregimen').filter(id_usuario__idtiporegimen__nombreregimen='Contributivo').annotate(cant_cont=Count('id_usuario__idtiporegimen'))
    regimensub=Casos.objects.values('id_usuario__idtiporegimen__nombreregimen').filter(id_usuario__idtiporegimen__nombreregimen='subsidiado').annotate(cant_sub=Count('id_usuario__idtiporegimen'))
    departamento=Casos.objects.values('id_usuario__cod_dep__nombre').annotate(cant_dep=Count('id_usuario__cod_dep'))
    municipio = Casos.objects.values('id_usuario__cod_muni__nombremunicipio').annotate(cant_mun=Count('id_usuario__cod_muni'))
    genero = Casos.objects.values('id_usuario__idgenero__nombregenero').annotate(cant_genero=Count('id_usuario__idgenero'))
    enfermedad=Casos.objects.values('enfermedad__nombreenfermedad').annotate(enfermedad=Count('enfermedad'))
    medicamentos=Casos.objects.values('id_comple_info__clasificacion_pbs__nombrepbs').annotate(medicamentos=Count('id_comple_info__clasificacion_pbs'))
    barrera=Casos.objects.values('id_barrera__nombre').annotate(barreras=Count('id_barrera'))
    
    for x in barrera:
        barr.append(x['id_barrera__nombre'])
        labelsbarr.append(x['barreras'])
    for x in medicamentos:
        medic.append(x['id_comple_info__clasificacion_pbs__nombrepbs'])
        labelsmedic.append(x['medicamentos'])
    for x in enfermedad:
        enfer.append(x['enfermedad__nombreenfermedad'])
        labelsenfe.append(x['enfermedad'])
    for x in genero:
        generos.append(x['id_usuario__idgenero__nombregenero'])
        labelsge.append(x['cant_genero'])
    for x in municipio:
        muni.append(x['id_usuario__cod_muni__nombremunicipio'])
        labelsmuni.append(x['cant_mun'])
    for z in departamento:
        depart.append(z['id_usuario__cod_dep__nombre'])
        labelsdep.append(z['cant_dep'])
    print(depart)
    for x in regimensub:
        sub.append(x['id_usuario__idtiporegimen__nombreregimen'])
        labelssub.append(x['cant_sub'])
    for x in regimencont:
        regcont.append(x['id_usuario__idtiporegimen__nombreregimen'])
        labelsregcont.append(x['cant_cont'])
    for r in regimen:
        reg.append(r['id_usuario__idtiporegimen__nombreregimen'])
        labelsreg.append(r['cant_reg'])
    for e in eps:
        epss.append(e['id_usuario__id_eps__nombre'])
        labelseps.append(e['cant_eps'])
    for abiertos in queryabierto:
        abierto.append(abiertos['estado__nombreestado'])
        labelsabierto.append(abiertos['cant_estado'])
    for abiertos in queryproceso:
        proceso.append(abiertos['estado__nombreestado'])
        labelsproceso.append(abiertos['cant_estado'])
    for abiertos in queryfinalizado:
        finalizado.append(abiertos['estado__nombreestado'])
        labelsfinalizado.append(abiertos['cant_estado'])
    for nestados in queryestados:
        estados.append(nestados['estado__nombreestado'])
        labelsestados.append(nestados['cant_estado'])
    print(epss)
    return render(request,'analista/graficas.html',
                  {
                   'labelsestados':labelsestados,
                   'estados':estados,
                   'labelsabierto':labelsabierto,
                   'abierto':abierto,
                   'labelsfinalizado':labelsfinalizado,
                   'finalizado':finalizado,
                   'labelsproceso':labelsproceso,
                   'proceso':proceso,
                   'labelseps':labelseps,
                   'EPS':epss,
                   'labelsreg':labelsreg,
                   'reg':reg,
                   'casos':casos,
                   'contributivo':regcont,
                   'labelscont':labelsregcont,
                   'subsidiado':labelssub,
                   'departamento':depart,
                   'labelsdep':labelsdep,
                   'municipio':muni,
                   'labelsmuni':labelsmuni,
                   'genero':generos,
                   'labelsge':labelsge,
                   'enfermedad':enfer,
                   'labelsenfer':labelsenfe,
                   'medic':medic,
                   'labelsmedic':labelsmedic,
                   'barrera':barr,
                   'labelsbarr':labelsbarr,
                   
                                                    })


@login_required
def get_data(request):
    proceso=[]
    labels=[]
    query= Casos.objects.values('estado__nombreestado').filter(estado__nombreestado='abierto').annotate(cant_estado=Count('estado'))
    for valor in query:
        proceso.append(valor['estado__nombreestado'])
        labels.append(valor['cant_estado'])
    print(proceso)
    print(labels)
    data={
        'proceso':proceso,
        'labels':labels
    }

    return JsonResponse(data)