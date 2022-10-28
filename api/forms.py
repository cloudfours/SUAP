from dataclasses import fields
from pyexpat import model
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from .models import *
class AsignacionTareaForm(forms.ModelForm):
    
     class Meta:
   
         model=AsignacionTarea
         fields=['id_gest','actividad','detalle','fecha','fech_registro','color','asginacion']
         labels={
             'id_gest':'Nombre del gestor',
             'actividad':'Actividad',
             'detalle':'Detalle de la actividad',
             'fecha':'Fecha',
             'fech_registro':'Fecha de registro',
             'color':'Color:',
             'asginacion':'Quien lo asigna'
             
         }
         widgets={
                   'id_gest':forms.Select(attrs={'class':'form-control'}),
                  'actividad':forms.TextInput(attrs={'class':'form-control'}),
                  'fecha':forms.DateInput(attrs={'class':'form-control datetimepicker-input','type':'date','placeholder':'ingrese fecha'},format='%Y-%m-%d'),
                  'fech_registro':forms.DateInput(attrs={'class':'form-control datetimepicker-input','type':'date','placeholder':'ingrese fecha'},format='%Y-%m-%d'),
                  'detalle':forms.Textarea(attrs={'class':'form-control '}),
                  'color':forms.TextInput(attrs={'class': 'form-control ','type':'color'}),
                  'asginacion':forms.TextInput(attrs={'class':'form-control '}),
                  
                 
        }
         
# class DateTimePickerInput(forms.DateTimeInput):
#         input_type = 'datetime'
class seguimientoFormulario(forms.ModelForm):
    class Meta:
        model=Seguimiento
        fields=['id_seg','id_gestor','fecharegistro','descripcion']
        labels={
            'id_seg':'seguimiento',
            'id_gestor':'Nombre del gestor',
            'fecharegistro':'Fecha de registro',
            'descripcion':'Descripcion'
        }
        widgets={
                   'id_seg':forms.NumberInput(attrs={'class':'form-control'}),
                  'id_gestor':forms.Select(attrs={'class':'form-control'}),
                  'fecharegistro':forms.DateInput(attrs={'class':'form-control datetimepicker-input','type':'date','placeholder':'ingrese fecha'},format='%Y-%m-%d'),
                  'descripcion':forms.Textarea(attrs={'class':'form-control '}),
        }
class informacionComplementaria(forms.ModelForm):
    class Meta:
        model = InfoComplementaria
        fields = ['id_comple','gestor_farma','terapia','otra_terapia','tipo_req','clasificacion_pbs','medico_trat','especialidad_med','segunda_barrera','fech_rad_for_eps','fecha_for_medi','fecha_aut','fech_rad_aut_farm','fecha_entrega','origen_soli','ips_id_terapia']
        labels={
            'id_comple':'Complementario',
            'gestor_farma':'Gestor farmaceutico',
            'terapia':'Terapia',
            'otra_terapia':'Otra terapia',
            'tipo_req':'Tipo de requerimiento',
            'clasificacion_pbs':'Clasificacion pbs',
            'medico_trat':'Medico tratante',
            'especialidad_med':'Especialidad Medica',
            'segunda_barrera':'Segunda barrera',
            'fech_rad_for_eps':'Fecha de radicacion de la  EPS',
            'fecha_for_medi':'fecha de la formula médica',
            'fecha_aut':'Fecha de autorizacion',
            'fech_rad_aut_farm':'Fecha de radicacion formula medica',
            'fecha_entrega':'Fecha de entrega',
            'origen_soli':'Origen de solicituda',
            'ips_id_terapia':'IPS'
            
        }
        widgets={
            # 'id_caso':forms.NumberInput(attrs={'class':'form-control'}),
            'id_comple':forms.NumberInput(attrs={'class':'form-control'}),
            'gestor_farma': forms.Select(attrs={'class':'form-control'}),
            'terapia': forms.Select(attrs={'class':'form-control'}),
            'otra_terapia':forms.TextInput(attrs={'class':'form-control'}),
            'tipo_req':forms.Select(attrs={'class':'form-control'}),
            'clasificacion_pbs':forms.Select(attrs={'class':'form-control'}),
            'medico_trat':forms.TextInput(attrs={'class':'form-control'}),
            'especialidad_med':forms.Select(attrs={'class':'form-control '}),
            'segunda_barrera':forms.TextInput(attrs={'class':'form-control'}),
            'fech_rad_for_eps':forms.DateInput(attrs={'class':'form-control datetimepicker-input','type':'datetime-local','placeholder':'ingrese fecha','required':False},format='%Y-%m-%d %H:%M'),
            'fecha_for_medi':forms.DateInput(attrs={'class':'form-control datetimepicker-input','type':'datetime-local','placeholder':'ingrese fecha'},format='%Y-%m-%d %H:%M'),
            'fecha_aut':forms.DateInput(attrs={'class':'form-control datetimepicker-input','type':'datetime-local','placeholder':'ingrese fecha'},format='%Y-%m-%d %H:%M'),
            'fech_rad_aut_farm':forms.DateInput(attrs={'class':'form-control datetimepicker-input','type':'datetime-local','placeholder':'ingrese fecha'},format='%Y-%m-%d %H:%M'),
            'fecha_entrega':forms.DateInput(attrs={'class':'form-control datetimepicker-input','type':'datetime-local','placeholder':'ingrese fecha'},format='%Y-%m-%d %H:%M'),
            'origen_soli':forms.TextInput(attrs={'class':'form-control'}),
            'ips_id_terapia':forms.Select(attrs={'class':'form-control'}),
        }
class EditarFormGestor(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['id_comple_info'].required=False
        self.fields['id_seguimiento'].required=False
        self.fields['fechaatenfinalizado'].required=False
        self.fields['fechaatenabierto'].required=False
        self.fields['fechaatenproceso'].required=False
       
    class Meta:
        model=Casos
       
        fields =['id_usuario','id_gest','estado','fecharesgistrocaso','fechaatenproceso','fechaatenfinalizado','fechaatenabierto','numeroradicado','descripcioncaso',
                 'enfermedad','fechaatencioneps','hora','id_comple_info','id_seguimiento','formula_medica','adjunto_seg','adjunto_terc'
                ,'id_barrera']
        #'id_comple_info','id_seguimiento','formula_medica','adjunto_pri'
        labels={
            # 'id_caso':'Caso',
            'id_gest':'Gestor',
            'estado':'Estado',
            'hora':'Hora',
            'fecharesgistrocaso':'Fecha registro',
            'fechaatenproceso':'Fecha Proceso',
            'fechaatenfinalizado':'Fecha Finalizado',
            'fechaatenabierto':'Fecha Abierto',
            'id_usuario':'Usuario',
            'numeroradicado':'Numero de radicado',
            'fechaatencioneps':'Fecha de atencion de EPS',
            'descripcioncaso':'Descripcion del caso',
            'enfermedad':'Enfermedad',
            'formula_medica':'Agregar Formula medico',
        
            'adjunto_seg':'Adjunto Segundo',
            'adjunto_terc':'Adjunto Tercero',
            'id_comple_info':'Información Complementaria',
            'id_seguimiento':'Seguimiento',
            'id_barrera':'Barrera',
        }
        widgets={
            # 'id_caso':forms.NumberInput(attrs={'class':'form-control'}),
            'id_usuario':forms.Select(attrs={'class':'form-control'}),
            'id_gest': forms.Select(attrs={'class':'form-control'}),
            'estado': forms.Select(attrs={'class':'form-control'}),
            'fecharesgistrocaso':forms.DateTimeInput(attrs={'class':'form-control datetimepicker-input','type':'datetime-local','placeholder':'ingrese fecha'},format='%Y-%m-%d %H:%M'),
            'fechaatenproceso':forms.DateTimeInput(attrs={'class':'form-control datetimepicker-input','type':'datetime-local','placeholder':'ingrese fecha','required':False},format='%Y-%m-%d %H:%M'),
            'fechaatenfinalizado':forms.DateTimeInput(attrs={'class':'form-control datetimepicker-input','type':'datetime-local','placeholder':'ingrese fecha','required':False},format='%Y-%m-%d %H:%M'),
            'fechaatenabierto':forms.DateTimeInput(attrs={'class':'form-control datetimepicker-input','type':'datetime-local','placeholder':'ingrese fecha','required':False},format='%Y-%m-%d %H:%M'),
            'numeroradicado':forms.NumberInput(attrs={'class':'form-control '}),
            'fechaatencioneps':forms.DateTimeInput(attrs={'class':'form-control datetimepicker-input','type':'datetime-local','placeholder':'ingrese fecha'},format='%Y-%m-%d %H:%M'),
            'descripcioncaso':forms.Textarea(attrs={'class':'form-control '}),
            'enfermedad':forms.Select(attrs={'class':'form-control '}),
            'formula_medica':forms.FileInput(attrs={'class':'form-control','multiple':True}),
          
            'adjunto_seg':forms.FileInput(attrs={'class':'form-control','multiple':True}),
            'adjunto_terc':forms.FileInput(attrs={'class':'form-control','multiple':True}),
            'id_comple_info':forms.Select(attrs={'class':'form-control'}),
            'id_seguimiento':forms.Select(attrs={'class':'form-control','default':'0'}),
            'id_barrera':forms.Select(attrs={'class':'form-control'}),
            'hora':forms.TimeInput(attrs={'class':'form-control'}),
        }

class CasosForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
     
    class Meta:
        model=Casos
        fields =['id_usuario','numeroradicado','descripcioncaso'
                 ,'enfermedad','fechaatencioneps','formula_medica','estado','fecharesgistrocaso'
                ,'id_barrera','id_seguimiento','id_comple_info']
        labels={
            # 'id_caso':'Caso',
            'id_usuario':'Usuario',
            'numeroradicado':'Numero de radicado',
            'fechaatencioneps':'Fecha de atencion de EPS',
            'descripcioncaso':'Descripcion del caso',
            'enfermedad':'Enfermedad',
            'formula_medica':'Agregar Formula medico',
            'id_barrera':'Barrera'
        }
        widgets={
            # 'id_caso':forms.NumberInput(attrs={'class':'form-control'}),
            'id_usuario':forms.Select(attrs={'class':'form-control'}),
            'numeroradicado':forms.NumberInput(attrs={'class':'form-control ','readonly':'readonly'}),
            'fechaatencioneps':forms.DateTimeInput(attrs={'class':'form-control datetimepicker-input','type':'datetime-local','placeholder':'ingrese fecha'},format='%Y-%m-%d %H:%M'),
            'fecharesgistrocaso':forms.DateTimeInput(attrs={'class':'form-control datetimepicker-input','type':'datetime-local','placeholder':'ingrese fecha'},format='%Y-%m-%d %H:%M'),
            'descripcioncaso':forms.Textarea(attrs={'class':'form-control '}),
            'enfermedad':forms.Select(attrs={'class':'form-control '}),
            'formula_medica':forms.FileInput(attrs={'class':'form-control'}),
            'id_barrera':forms.Select(attrs={'class':'form-control'}),
             'estado':forms.Select(attrs={'class':'form-control'}),
        }
   
class datosuserFormEdit(forms.ModelForm):
    #   def __init__(self,*args,disabled_select=None,**kwargs):
    #      super(datosuserForm, self).__init__(*args,**kwargs)
    #      if self.disabled_select:
    #         self.fields['tipo_doc'].widget.disabled_select = disabled_select;
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # self.fields['tipo_doc'].disabled = True
            # if self.fields['id_eps'] is None:
            #     self.fields['id_eps'].disabled = False
            # else:
            #     self.fields['id_eps'].disabled = True
      
    
    class Meta:
        model = DatosUsuario
       
        fields = ['id_cedula', 'primer_nombre', 'primer_apellido', 'segundo_nombre', 'segundo_apellido', 'tipo_doc','tipo_envio','celular','direccion','id_eps','idtiporegimen','idgenero'
                   ,'cod_pais','cod_dep','cod_muni','fechanaci','ocupacion','id_grupo_etnico','id_poblacion_especial']
        labels = {
            'id_cedula': 'Numero de documento',
            'primer_nombre': 'Primer nombre',
            'primer_apellido': 'Primer apellido',
            'segundo_nombre': 'Segundo nombre',
            'segundo_apellido': 'Segundo apellido',
            'tipo_doc': 'Tipo de documento',
            'tipo_envio':'Tipo de envio',
            'celular':'Celular',
            'direccion':'Direccion',
            'id_eps':'EPS',
            'idtiporegimen':'Tipo de regimen',
            'idgenero':'Genero',
            'cod_pais':'Pais',
            'cod_dep':'Departamento',
            'cod_muni':'Municipio',
            'fechanaci':'Fecha de nacimiento',
            'ocupacion':'Ocupacion',
            'id_grupo_etnico':'Grupo Etnico',
            'id_poblacion_especial':'Poblacion especial'
            
        }
        widgets = {
            'id_cedula': forms.NumberInput(attrs={'class': 'form-control is-valid','readonly':'readonly'}),
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control is-valid','id':'floatingInputInvalid','placeholder':'Ingrese su nombre'}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'tipo_doc': forms.Select(attrs={'class': 'form-select is-valid','readonly': 'readonly'}),
            'tipo_envio':forms.Select(attrs={'class': 'form-select is-valid'}),
            'celular':forms.NumberInput(attrs={'class': 'form-control is-valid','max_length':'100','placeholder':'ingrese numero de celular'}),
            'direccion':forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'id_eps':forms.Select(attrs={'class': 'form-select  is-valid'}),
            'idtiporegimen':forms.Select(attrs={'class': 'form-select is-valid'}),
            'idgenero':forms.Select(attrs={'class': 'form-select is-valid'}),
            'cod_pais':forms.Select(attrs={'class': 'form-select is-valid'}),
            'cod_dep':forms.Select(attrs={'class': 'form-select is-valid'}),
            'cod_muni':forms.Select(attrs={'class': 'form-select is-valid'}),
            'fechanaci':forms.DateInput(attrs={'class': 'form-control is-valid'},format=('%Y-%m-%d')),
            'ocupacion': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'id_grupo_etnico':forms.Select(attrs={'class': 'form-select is-valid'}),
            'id_poblacion_especial':forms.Select(attrs={'class': 'form-select is-valid'})
            
        }
  

class datosuserForm(forms.ModelForm):
    class Meta:
        model = DatosUsuario
        fields = ['id_cedula', 'primer_nombre', 'primer_apellido', 'segundo_nombre', 'segundo_apellido', 'tipo_doc']
        labels = {
            'id_cedula': 'Numero de documento',
            'primer_nombre': 'Primer nombre',
            'primer_apellido': 'Primer apellido',
            'segundo_nombre': 'Segundo nombre',
            'segundo_apellido': 'Segundo apellido',
            'tipo_doc': 'Tipo de documento'
        }
        widgets = {
            'id_cedula': forms.NumberInput(attrs={'class': 'form-control is-valid'}),
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'tipo_doc': forms.Select(attrs={'class': 'form-select is-valid'}),
        }

    # se hace la validacion del usuario con UnicodeUnsernameValidoe(


username_validator = UnicodeUsernameValidator()


class userRegister(UserCreationForm):
    email = forms.EmailField(label=_('Correo'), max_length=50, help_text='Required. Correo invalido.',
                             widget=(forms.TextInput(attrs={'class': 'form-control is-valid'})))
    password1 = forms.CharField(label=_('Contraseña'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control is-valid'})),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=_('Contraseña  confirmation'),
                                widget=forms.PasswordInput(attrs={'class': 'form-control is-valid'}),
                                help_text=_('Confirme contraseña'))
    username = forms.CharField(
        label=_('Usuario'),
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={'unique': _("A user with that username already exists.")},
        widget=forms.TextInput(attrs={'class': 'form-control is-valid'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
