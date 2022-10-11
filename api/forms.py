from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from .models import *
import re
# class DateTimePickerInput(forms.DateTimeInput):
#         input_type = 'datetime'
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
            'estado':forms.Select(attrs={'class':'form-control'}),
            'numeroradicado':forms.NumberInput(attrs={'class':'form-control '}),
            'fechaatencioneps':forms.DateTimeInput(attrs={'class':'form-control datetimepicker-input','type':'datetime-local','placeholder':'ingrese fecha'},format='%Y-%m-%d %H:%M:%S'),
            'fecharesgistrocaso':forms.DateTimeInput(attrs={'class':'form-control datetimepicker-input','type':'datetime-local','placeholder':'ingrese fecha'},format='%Y-%m-%d %H:%M:%S'),
            'descripcioncaso':forms.Textarea(attrs={'class':'form-control '}),
            'enfermedad':forms.Select(attrs={'class':'form-control '}),
            'formula_medica':forms.FileInput(attrs={'class':'form-control'}),
            'id_barrera':forms.Select(attrs={'class':'form-control'}),
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
                                widget=(forms.PasswordInput(attrs={'class': 'form-control is-valid','id':'contrasena'})),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=_('Contraseña  confirmar'),
                                widget=forms.PasswordInput(attrs={'class': 'form-control is-valid'}),
                                help_text=_('Confirme contraseña'))
    username = forms.CharField(
        label=_('Usuario'),
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={'unique': _("A user with that username already exists.")},
        widget=forms.TextInput(attrs={'class': 'form-control is-valid','id':'username'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
    def clean(self,*args,**kwargs):
        clean_data=super(userRegister,self).clean(*args,**kwargs)
        contrasena = clean_data.get('Contraseña',None)
        if contrasena ==' ':
            self.add_error('contraseña','invalida')