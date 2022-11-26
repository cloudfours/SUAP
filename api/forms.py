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
         fields=['id_gest','actividad','detalle','fecha','fech_registro','prioridad','asginacion']
         labels={
             'id_gest':'Nombre del gestor',
             'actividad':'Actividad',
             'detalle':'Detalle de la actividad',
             'fecha':'Fecha programada',
             'fech_registro':'Fecha de registro',
             'prioridad':'Prioridad:',
             'asginacion':'Quien lo asigna'
             
         }
         widgets={
                   'id_gest':forms.Select(attrs={'class':'form-control'}),
                  'actividad':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese tipo de actividad'}),
                  'fecha':forms.DateInput(attrs={'class':'form-control is-valid','type':'date','placeholder':'ingrese fecha','required':False},format='%Y-%m-%d'),
                  'fech_registro':forms.DateInput(attrs={'class':'form-control is-valid','type':'date','placeholder':'ingrese fecha','required':False},format='%Y-%m-%d'),
                  'detalle':forms.Textarea(attrs={'class':'form-control is-valid','placeholder':'Ingrese detalle'}),
                  'prioridad':forms.RadioSelect(),
                  'asginacion':forms.TextInput(attrs={'class':'form-control is-valid','placeholder':'Ingrese su quien lo asigna'}),
                  
                 
        }
         
# class DateTimePickerInput(forms.DateTimeInput):
#         input_type = 'datetime'
class seguimientoFormulario(forms.ModelForm):
    class Meta:
        model=Seguimiento
        fields=['id_seg','id_gestor','fecharegistro','descripcion']
        labels={
            'id_seg':'Seguimiento',
            'id_gestor':'Nombre del gestor',
            'fecharegistro':'Fecha de registro',
            'descripcion':'Descripción'
        }
        widgets={
                   'id_seg':forms.NumberInput(attrs={'class':'form-control'}),
                  'id_gestor':forms.Select(attrs={'class':'form-control is-valid'}),
                  'fecharegistro':forms.DateInput(attrs={'class':'form-control is-valid','type':'date','placeholder':'ingrese fecha'},format='%Y-%m-%d'),
                  'descripcion':forms.Textarea(attrs={'class':'form-control is-valid','placeholder':'Ingrese descripción del seguimiento'}),
        }
class informacionComplementaria(forms.ModelForm):
    class Meta:
        model = InfoComplementaria
        fields = ['id_comple','gestor_farma','terapia','otra_terapia','tipo_req','clasificacion_pbs','medico_trat','especialidad_med','segunda_barrera','fech_rad_for_eps','fecha_for_medi','fecha_aut','fech_rad_aut_farm','fecha_entrega','origen_soli','ips_id_terapia']
        labels={
            'id_comple':'Complementario',
            'gestor_farma':'Gestor farmacéutico',
            'terapia':'Terapia',
            'otra_terapia':'Otra terapia',
            'tipo_req':'Tipo de requerimiento',
            'clasificacion_pbs':'Clasificación pbs',
            'medico_trat':'Medico tratante',
            'especialidad_med':'Especialidad Medica',
            'segunda_barrera':'Segunda barrera',
            'fech_rad_for_eps':'Fecha de radicación de la  EPS',
            'fecha_for_medi':'fecha de la formula médica',
            'fecha_aut':'Fecha de autorización',
            'fech_rad_aut_farm':'Fecha de radicación formula medica',
            'fecha_entrega':'Fecha de entrega',
            'origen_soli':'Origen de solicitud',
            'ips_id_terapia':'IPS'
            
        }
        widgets={
            # 'id_caso':forms.NumberInput(attrs={'class':'form-control'}),
            'id_comple':forms.NumberInput(attrs={'class':'form-control is-valid'}),
            'gestor_farma': forms.Select(attrs={'class':'form-control is-valid'}),
            'terapia': forms.Select(attrs={'class':'form-control is-valid'}),
            'otra_terapia':forms.TextInput(attrs={'class':'form-control is-valid','placeholder':'Ingrese otro tipo de terapia'}),
            'tipo_req':forms.Select(attrs={'class':'form-control is-valid'}),
            'clasificacion_pbs':forms.Select(attrs={'class':'form-control is-valid'}),
            'medico_trat':forms.TextInput(attrs={'class':'form-control is-valid','placeholder':'Ingrese su medico tratante'}),
            'especialidad_med':forms.Select(attrs={'class':'form-control is-valid','required':True }),
            'segunda_barrera':forms.TextInput(attrs={'class':'form-control is-valid'}),
            'fech_rad_for_eps':forms.DateInput(attrs={'class':'form-control is-valid','type':'date','placeholder':'ingrese fecha','required':False},format='%Y-%m-%d'),
            'fecha_for_medi':forms.DateInput(attrs={'class':'form-control is-valid','type':'date','placeholder':'ingrese fecha'},format='%Y-%m-%d '),
            'fecha_aut':forms.DateInput(attrs={'class':'form-control is-valid','type':'date','placeholder':'ingrese fecha'},format='%Y-%m-%d '),
            'fech_rad_aut_farm':forms.DateInput(attrs={'class':'form-control is-valid','type':'date','placeholder':'ingrese fecha'},format='%Y-%m-%d'),
            'fecha_entrega':forms.DateInput(attrs={'class':'form-control is-valid','type':'date','placeholder':'ingrese fecha'},format='%Y-%m-%d'),
            'origen_soli':forms.TextInput(attrs={'class':'form-control is-valid'}),
            'ips_id_terapia':forms.Select(attrs={'class':'form-control is-valid'}),
        }
class EditarFormGestor(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['fechaatenfinalizado'].required=False
        self.fields['fechaatenabierto'].required=False
        self.fields['fechaatenproceso'].required=False
        self.fields['formula_medica'].required=False
        self.fields['adjunto_seg'].required=False
        self.fields['adjunto_terc'].required=False

     
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
            'fechaatenproceso':'Fecha proceso',
            'fechaatenfinalizado':'Fecha finalizado',
            'fechaatenabierto':'Fecha abierto',
            'id_usuario':'Usuario',
            'numeroradicado':'Número de radicado',
            'fechaatencioneps':'Fecha de atención de EPS',
            'descripcioncaso':'Descripción del caso',
            'enfermedad':'Enfermedad',
            'formula_medica':'Agregar fórmula médica',
        
            'adjunto_seg':'Adjunto segundo',
            'adjunto_terc':'Adjunto tercero',
            'id_comple_info':'Información complementaria',
            'id_seguimiento':'Seguimiento',
            'id_barrera':'Barrera',
        }
        widgets={
            # 'id_caso':forms.NumberInput(attrs={'class':'form-control'}),
            'id_usuario':forms.Select(attrs={'class':'form-control is-valid'}),
            'id_gest': forms.Select(attrs={'class':'form-control is-valid'}),
            'estado': forms.Select(attrs={'class':'form-control is-valid'}),
            'fecharesgistrocaso':forms.DateInput(attrs={'class':'form-control is-valid','type':'date','placeholder':'ingrese fecha'},format='%Y-%m-%d'),
            'fechaatenproceso':forms.DateInput(attrs={'class':'form-control is-valid','type':'date','placeholder':'ingrese fecha'},format='%Y-%m-%d'),
            'fechaatenfinalizado':forms.DateInput(attrs={'class':'form-control is-valid','type':'date','placeholder':'ingrese fecha'},format='%Y-%m-%d'),
            'fechaatenabierto':forms.DateInput(attrs={'class':'form-control is-valid','type':'date','placeholder':'ingrese fecha'},format='%Y-%m-%d'),
            'numeroradicado':forms.NumberInput(attrs={'class':'form-control is-valid','readonly':'readonly'}),
            'fechaatencioneps':forms.DateInput(attrs={'class':'form-control is-valid','type':'date','placeholder':'ingrese fecha'},format='%Y-%m-%d'),
            'descripcioncaso':forms.Textarea(attrs={'class':'form-control is-valid','placeholder':'Ingrese descripción del caso'}),
            'enfermedad':forms.Select(attrs={'class':'form-control is-valid','placeholder':'Ingrese su enfermedad'}),
            'formula_medica':forms.FileInput(attrs={'class':'form-control','multiple':True}),
          
            'adjunto_seg':forms.FileInput(attrs={'class':'form-control','multiple':True}),
            'adjunto_terc':forms.FileInput(attrs={'class':'form-control','multiple':True}),
            'id_comple_info':forms.Select(attrs={'class':'form-control'}),
            'id_seguimiento':forms.Select(attrs={'class':'form-control','default':'0'}),
            'id_barrera':forms.Select(attrs={'class':'form-control is-valid'}),
            'hora':forms.TimeInput(attrs={'class':'form-control is-valid','type':'time'}),
        }

class CasosForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    
     
    class Meta:
        model=Casos
        fields =['id_usuario','numeroradicado','descripcioncaso'
                 ,'enfermedad','fechaatencioneps','formula_medica','estado','fecharesgistrocaso'
                ,'id_barrera']
        labels={
            # 'id_caso':'Caso',
            'id_usuario':'Usuario',
            'numeroradicado':'Número de radicado',
            'fechaatencioneps':'Fecha de atención de EPS',
            'descripcioncaso':'Descripción del caso',
            'enfermedad':'Enfermedad',
            'formula_medica':'Agregar fórmula médica',
            'id_barrera':'Barrera'
        }
        widgets={
            # 'id_caso':forms.NumberInput(attrs={'class':'form-control'}),
            'id_usuario':forms.Select(attrs={'class':'form-control is-valid'}),
            'numeroradicado':forms.NumberInput(attrs={'class':'form-control is-valid','readonly':'readonly'}),
            'fechaatencioneps':forms.DateInput(attrs={'class':'form-control is-valid','type':'date','placeholder':'ingrese fecha'}),
            'fecharesgistrocaso':forms.DateInput(attrs={'class':'form-control is-valid','type':'date','placeholder':'ingrese fecha'},format='%Y-%m-%d'),
            'descripcioncaso':forms.Textarea(attrs={'class':'form-control is-valid','placeholder':'Ingrese descripción del caso'}),
            'enfermedad':forms.Select(attrs={'class':'form-control is-valid','placeholder':'Ingrese su enfermedad'}),
            'formula_medica':forms.FileInput(attrs={'class':'form-control','lang':"es"}),
            'id_barrera':forms.Select(attrs={'class':'form-control is-valid'}),
             'estado':forms.Select(attrs={'class':'form-control is-valid'}),
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
            'id_cedula': 'Número de documento',
            'primer_nombre': 'Primer nombre',
            'primer_apellido': 'Primer apellido',
            'segundo_nombre': 'Segundo nombre',
            'segundo_apellido': 'Segundo apellido',
            'tipo_doc': 'Tipo de documento',
            'tipo_envio':'Tipo de envió',
            'celular':'Celular',
            'direccion':'Dirección',
            'id_eps':'EPS',
            'idtiporegimen':'Tipo de regimen',
            'idgenero':'Género',
            'cod_pais':'País',
            'cod_dep':'Departamento',
            'cod_muni':'Municipio',
            'fechanaci':'Fecha de nacimiento',
            'ocupacion':'Ocupación',
            'id_grupo_etnico':'Grupo étnico',
            'id_poblacion_especial':'Población especial'
            
        }
        widgets = {
            'id_cedula': forms.NumberInput(attrs={'class': 'form-control is-valid','readonly':'readonly','min':"1"}),
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control is-valid','id':'floatingInputInvalid','placeholder':'Ingrese su nombre'}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control is-valid','placeholder':'Ingrese su primer apellido' }),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control is-valid','placeholder':'Ingrese su segundo nombre'}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control is-valid','placeholder':'Ingrese su segundo apellido'}),
            'tipo_doc': forms.Select(attrs={'class': 'form-select is-valid','readonly': 'readonly'}),
            'tipo_envio':forms.Select(attrs={'class': 'form-select is-valid'}),
            'celular':forms.NumberInput(attrs={'class': 'form-control is-valid','max_length':'100','placeholder':'ingrese numero de celular'}),
            'direccion':forms.TextInput(attrs={'class': 'form-control is-valid','placeholder':'Ingrese su dirección'}),
            'id_eps':forms.Select(attrs={'class': 'form-select  is-valid'}),
            'idtiporegimen':forms.Select(attrs={'class': 'form-select is-valid'}),
            'idgenero':forms.Select(attrs={'class': 'form-select is-valid'}),
            'cod_pais':forms.Select(attrs={'class': 'form-select is-valid'}),
            'cod_dep':forms.Select(attrs={'class': 'form-select is-valid'}),
            'cod_muni':forms.Select(attrs={'class': 'form-select is-valid'}),
            'fechanaci':forms.DateInput(attrs={'class': 'form-control is-valid','type':'date'},format=('%Y-%m-%d')),
            'ocupacion': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'id_grupo_etnico':forms.Select(attrs={'class': 'form-select is-valid'}),
            'id_poblacion_especial':forms.Select(attrs={'class': 'form-select is-valid'})
            
        }
  

class datosuserForm(forms.ModelForm):
    class Meta:
        model = DatosUsuario
        fields = ['id_cedula', 'primer_nombre', 'primer_apellido', 'segundo_nombre', 'segundo_apellido', 'tipo_doc']
        labels = {
            'id_cedula': 'Número de documento',
            'primer_nombre': 'Primer nombre',
            'primer_apellido': 'Primer apellido',
            'segundo_nombre': 'Segundo nombre',
            'segundo_apellido': 'Segundo apellido',
            'tipo_doc': 'Tipo de documento',
           
        }
        widgets = {
            'id_cedula': forms.NumberInput(attrs={'class': 'form-control is-valid','placeholder':'Ingrese su numero de identificacion'}),
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control is-valid','placeholder':'Ingrese su primer nombre'}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control is-valid','placeholder':'Ingrese su primer apellido'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control is-valid','placeholder':'Ingrese su segundo nombre'}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control is-valid','placeholder':'Ingrese su segundo apellido'}),
            'tipo_doc': forms.Select(attrs={'class': 'form-select is-valid'}),
            'trata_data':forms.RadioSelect(attrs={'class': ''}),
        }

    # se hace la validacion del usuario con UnicodeUnsernameValidoe(


username_validator = UnicodeUsernameValidator()


class userRegister(UserCreationForm):
    email = forms.EmailField(label=_('Correo'), max_length=50, help_text='Required. Correo invalido.',
                             widget=(forms.TextInput(attrs={'class': 'form-control is-valid','placeholder':'Ingrese su correo'})))
    password1 = forms.CharField(label=_('Contraseña'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control is-valid','placeholder':'Ingrese una contraseña'})),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=_('Confirme contraseña'),
                                widget=forms.PasswordInput(attrs={'class': 'form-control is-valid','placeholder':'Confirme contraseña'}),
                                help_text=_('Confirme contraseña'))
    username = forms.CharField(
        label=_('Usuario'),
        max_length=150,
        help_text=_('requiere. 150 caracteres o meno. letras, digitos and @/./+/-/_ solamente.'),
        validators=[username_validator],
        error_messages={'unique': _("el usuario ya existe.")},
        widget=forms.TextInput(attrs={'class': 'form-control is-valid','placeholder':'Ingrese nombre usuario'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     qs = User.objects.filter(email=email)
    #     if qs.exists():
    #         raise forms.ValidationError("La direccion email ya existe")
    #     return email
