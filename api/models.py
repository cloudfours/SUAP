from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField
from django.forms import model_to_dict
# se emigra todas las tablas y se convierten en modelos de clase como una plantilla
class Analista(models.Model):
    analista_id = models.SmallAutoField(primary_key=True)
    id_datos_us = models.ForeignKey('DatosUsuario', models.DO_NOTHING, db_column='id_datos_us')


 





class BarreraAcceso(models.Model):
    id_barrera_acceso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)


    def __str__(self):
        return f'{self.nombre}'


class Casos(models.Model):
    id_caso =  models.AutoField(primary_key=True,db_column='id_caso')
    id_usuario = models.ForeignKey('DatosUsuario', models.DO_NOTHING, db_column='id_usuario')
    id_gest = models.ForeignKey('GestorCaso', models.DO_NOTHING, db_column='id_gest')
    numeroradicado = models.PositiveIntegerField(db_column='numeroRadicado')  # Field name made lowercase.
    fechaatencioneps = models.DateField(db_column='fechaAtencionEps')  # Field name made lowercase.
    descripcioncaso = models.TextField(db_column='descripcionCaso')  # Field name made lowercase.
  
    estado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='estado')
    fecharesgistrocaso = models.DateField(db_column='fechaResgistroCaso', blank=True,
                                              null=True)  # Field name made lowercase.
    enfermedad = models.ForeignKey('TipoEnfermedad', models.DO_NOTHING, db_column='enfermedad', blank=True)
    fechaatenproceso = models.DateField(db_column='fechaAtenProceso',
                                            null=True)  # Field name made lowercase.
    fechaatenfinalizado = models.DateField(db_column='fechaAtenFinalizado', 
                                               null=True,)  # Field name made lowercase.
    fechaatenabierto = models.DateField(db_column='fechaAtenAbierto', 
                                            null=True,)# Field name made lowercase.
    hora = models.TimeField( null=True)
    formula_medica = models.FileField(upload_to='uploads/',blank=True, null=True)

    adjunto_seg = models.FileField(upload_to='uploads/',blank=True, null=True)
    adjunto_terc = models.FileField(upload_to='uploads/',blank=True, null=True)
    id_comple_info = models.OneToOneField('InfoComplementaria', models.DO_NOTHING, db_column='id_comple_info', blank=True,
                                       null=True)
    id_seguimiento = models.OneToOneField('Seguimiento', models.DO_NOTHING, db_column='id_seguimiento',blank=True, null=True)
    id_barrera = models.ForeignKey(BarreraAcceso, models.DO_NOTHING, db_column='id_barrera')
    class Estado_activo(models.TextChoices):
        activo='1',_('activo')
        inactivo='0',_('inactivo')
    estado_pendiente=models.CharField(max_length=8,choices=Estado_activo.choices,default=Estado_activo.activo)
    def clean(self):
         self.descripcioncaso=self.descripcioncaso.capitalize()




class ClasificacionPbs(models.Model):
    id_pbs = models.AutoField(primary_key=True)
    nombrepbs = models.CharField(db_column='nombrePbs', max_length=60)  # Field name made lowercase.
    def __str__(self):
        return f'{self.nombrepbs}'





    


class DatosUsuario(models.Model):
    id_cedula = models.PositiveIntegerField(db_column='id_cedula', primary_key=True)  # Field name made lowercase.
    primer_nombre = models.CharField(max_length=40, blank=True, null=True)
    primer_apellido = models.CharField(max_length=40, blank=True, null=True)
    segundo_nombre = models.CharField(max_length=40, blank=True, null=True)
    segundo_apellido = models.CharField(max_length=40, blank=True, null=True)
    tipo_doc = models.ForeignKey('TipoDocumento', models.DO_NOTHING, db_column='tipo_doc')
    celular = models.BigIntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=40, blank=True, null=True)
    id_eps = models.ForeignKey('Eps', models.DO_NOTHING, db_column='id_EPS')  # Field name made lowercase.
    idtiporegimen = models.ForeignKey('Regimen', models.DO_NOTHING,
                                      db_column='IdTipoRegimen')  # Field name made lowercase.
    idgenero = models.ForeignKey('Genero', models.DO_NOTHING, db_column='idGenero', blank=True,
                                 null=True)  # Field name made lowercase.
    cod_pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='cod_pais')
    cod_dep = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='cod_dep')
    cod_muni = models.ForeignKey('municipio', models.DO_NOTHING, db_column='cod_muni')
    fechanaci = models.DateField(db_column='fechaNaci', blank=True, null=True)  # Field name made lowercase.
    ocupacion = models.CharField(max_length=40, blank=True, null=True)
    tipo_envio = models.ForeignKey('EnvioAlertas', models.DO_NOTHING, db_column='tipo_envio')
    id_grupo_etnico = models.ForeignKey('GrupoEtnico', models.DO_NOTHING, db_column='id_grupo_etnico')
    id_poblacion_especial = models.ForeignKey('PoblacionEspecial', models.DO_NOTHING, db_column='id_poblacion_especial')
    login_id = models.OneToOneField(User, on_delete=models.CASCADE,db_column='login_id')
    def __str__(self):
        return f'{self.id_cedula}'


class Departamento(models.Model):
    cod_dep = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=10, blank=True, null=True)


    
    def __str__(self):
        return f'{self.cod_dep} - {self.nombre}'
    def clean(self):
        self.nombre=self.nombre.capitalize()

class Enuesta(models.Model):
    idencuesta = models.SmallAutoField(primary_key=True)
    evaluacionres = models.CharField(db_column='evaluacionRes', max_length=40, blank=True,
                                     null=True)  # Field name made lowercase.
    evaliaciongestor = models.IntegerField(db_column='evaliacionGestor', blank=True,
                                           null=True)  # Field name made lowercase.
    idusuario = models.ForeignKey(DatosUsuario, models.DO_NOTHING, db_column='idUsuario', blank=True,
                                  null=True)  # Field name made lowercase.

   


class EnvioAlertas(models.Model):
    tipoenvio = models.CharField(db_column='tipoEnvio', max_length=40)  # Field name made lowercase.
    id_envio = models.SmallAutoField(primary_key=True)
    def __str__(self):
        return f'{self.tipoenvio}'

    def clean(self):
        self.tipoenvio=self.tipoenvio.capitalize()


class Eps(models.Model):
    cod_eps = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15, blank=True, null=True)

    
    def __str__(self):
        return f'{self.cod_eps} {self.nombre}'
    def clean(self):
        self.nombre=self.nombre.capitalize()

class EspecialidadMed(models.Model):
    id_esp = models.SmallAutoField(db_column='id_esp',primary_key=True)
    nombre = models.CharField(db_column='nombre',max_length=40)
    def __str__(self):
        return f'{self.nombre}'
    def clean(self):
        self.nombre=self.nombre.capitalize()



class Estado(models.Model):
    idestado = models.AutoField(db_column='idEstado', primary_key=True)  # Field name made lowercase.
    nombreestado = models.CharField(db_column='nombreEstado', max_length=15)  # Field name made lowercase.
    
    def __str__(self):
        return f'{self.nombreestado}'
    def clean(self):
        self.nombreestado=self.nombreestado.capitalize()
   


class Genero(models.Model):
    idgenero = models.PositiveIntegerField(db_column='idGenero', primary_key=True)  # Field name made lowercase.
    nombregenero = models.CharField(db_column='nombreGenero', max_length=5)  # Field name made lowercase.

  
    def __str__(self):
        return f'{self.idgenero} - {self.nombregenero}'
    


class GestorCaso(models.Model):
    id_gest = models.SmallAutoField(db_column='Id_gest', primary_key=True)  # Field name made lowercase.
    cantcasos = models.SmallIntegerField(db_column='cantCasos', blank=True, null=True)  # Field name made lowercase.
    id_datos_us = models.ForeignKey(DatosUsuario, models.DO_NOTHING, db_column='id_datos_us', blank=True, null=True)
   

    def __str__(self):
        return f'{self.id_datos_us.primer_nombre}'
    
    
class AsignacionTarea(models.Model):
    id_gest = models.ForeignKey(GestorCaso, models.DO_NOTHING, db_column='id_gest', blank=True, null=True)
    asginacion = models.CharField(max_length=255,blank=True,null=True)
    actividad = models.CharField(max_length=40, blank=True, null=True)
    detalle= models.TextField(db_column='detalle',default='')
    fecha = models.DateField()
    fech_registro = models.DateField()
    class Estado_activo_actividad(models.TextChoices):
            activo='1',_('activo')
            inactivo='0',_('inactivo')
    estado_pendiente=models.CharField(max_length=8,choices=Estado_activo_actividad.choices,default=Estado_activo_actividad.activo, blank=True,null=True)
    class prioridad(models.TextChoices):
        activo='Alta',_('Alta')
        inactivo='Media',_('Media')
        baja='Baja',_('Baja')
    prioridad=models.CharField(max_length=10,choices=prioridad.choices,default=prioridad.baja, blank=True,null=True)
    def toJSON(self):
        item = model_to_dict(self)
        return item
    def __str__(self):
        return f'{self.id}'
class GestorFarmacia(models.Model):
    id_far = models.AutoField(primary_key=True)
    nombrefarmacia = models.CharField(db_column='nombreFarmacia', max_length=40)  # Field name made lowercase.
    def __str__(self):
        return f'{self.nombrefarmacia}'
    def clean(self):
        self.nombrefarmacia=self.nombrefarmacia.capitalize()



class GrupoEtnico(models.Model):
    id_gr_etn = models.PositiveIntegerField(primary_key=True)
    nombreetnico = models.CharField(db_column='nombreEtnico', max_length=40)  # Field name made lowercase.

    
    def __str__(self) -> str:
        return f'{self.nombreetnico}'
    def clean(self):
        self.nombreetnico=self.nombreetnico.capitalize()

class IndicadoresGestion(models.Model):
    id_ind_ges = models.PositiveSmallIntegerField()
    idusuario = models.ForeignKey(DatosUsuario, models.DO_NOTHING, db_column='idUsuario')  # Field name made lowercase.
    tiempores = models.DateField(db_column='tiempoRes', blank=True, null=True)  # Field name made lowercase.
    resolutividad = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

   


class InfoComplementaria(models.Model):
    id_comple = models.SmallAutoField(primary_key=True)
    gestor_farma = models.ForeignKey(GestorFarmacia, models.DO_NOTHING, db_column='gestor_farma',blank=True, null=True)
    terapia = models.ForeignKey('Terapia', models.DO_NOTHING, db_column='terapia',blank=True, null=True)
    otra_terapia = models.CharField(max_length=50, blank=True, null=True)
    tipo_req = models.ForeignKey('TipReq', models.DO_NOTHING, db_column='tipo_req', blank=True, null=True)
    clasificacion_pbs = models.ForeignKey(ClasificacionPbs, models.DO_NOTHING ,blank=True, null=True)
    medico_trat = models.CharField(max_length=40)
    especialidad_med = models.ForeignKey(EspecialidadMed, models.DO_NOTHING, db_column='especialidad_med',blank=True, null=True)
    segunda_barrera = models.CharField(max_length=40)
    fech_rad_for_eps = models.DateField(db_column='fech_rad_for_EPS',blank=True, null=True)  # Field name made lowercase.
    fecha_for_medi = models.DateField(blank=True, null=True)
    fecha_aut = models.DateField(blank=True, null=True)
    fech_rad_aut_farm = models.DateField(blank=True, null=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    origen_soli = models.CharField(max_length=40)
    ips_id_terapia = models.ForeignKey('Ips', models.DO_NOTHING, db_column='ips_id_terapia',blank=True, null=True)
    def __str__(self):
        return f'{self.id_comple}'

    def clean(self):
        self.otra_terapia=self.otra_terapia.capitalize()
        self.origen_soli=self.origen_soli.capitalize()
        self.medico_trat=self.medico_trat.capitalize()


class Ips(models.Model):
    id_terapia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    def __str__(self):
        return f'{self.nombre}'
    def clean(self):
        self.nombre=self.nombre.capitalize()
  






class Municipio(models.Model):
    cod_municipio = models.PositiveSmallIntegerField(primary_key=True)
    nombremunicipio = models.CharField(db_column='nombreMunicipio', max_length=15, blank=True,
                                       null=True)  # Field name made lowercase.
   


    def __str__(self):
        return f'{self.cod_municipio} {self.nombremunicipio}'
    def clean(self):
        self.nombremunicipio=self.nombremunicipio.capitalize()

class PacienteUsuario(models.Model):
    id_paciente = models.SmallAutoField(primary_key=True)
    numusu = models.SmallIntegerField(db_column='numUsu', blank=True, null=True)  # Field name made lowercase.
    id_dat_us = models.ForeignKey(DatosUsuario, models.DO_NOTHING, db_column='id_dat_us', blank=True, null=True)





class Pais(models.Model):
    cod_pais = models.SmallAutoField(primary_key=True)
    nombrepais = models.CharField(db_column='nombrePais', max_length=40)  # Field name made lowercase.


    def __str__(self) -> str:
        ""
        ""
        return f'{self.cod_pais} {self.nombrepais}'
    def clean(self):
        self.nombre=self.nombrepais.capitalize()

class PoblacionEspecial(models.Model):
    id_pb_esp = models.PositiveIntegerField(primary_key=True)
    nombrepoblacionesp = models.CharField(db_column='nombrePoblacionEsp', max_length=40, blank=True,
                                          null=True)  # Field name made lowercase.


    
    def __str__(self)->str:
        return f'{self.id_pb_esp} {self.nombrepoblacionesp}'
    def clean(self):
        self.nombrepoblacionesp=self.nombrepoblacionesp.capitalize()

class Regimen(models.Model):
    cod_regimen = models.PositiveIntegerField(primary_key=True)
    nombreregimen = models.CharField(db_column='nombreRegimen', max_length=15)  # Field name made lowercase.

 
    def __str__(self):
        return f'{self.cod_regimen} - {self.nombreregimen}'
    def clean(self):
        self.nombreregimen = self.nombreregimen.capitalize()

class TipoDocumento(models.Model):
    id_doc = models.AutoField(primary_key=True)
    nombredocumento = models.CharField(db_column='nombreDocumento', max_length=40)  # Field name made lowercase.

 

    def __str__(self):
        return f'{self.nombredocumento}'
    def clean(self):
        self.nombredocumento=self.nombredocumento.capitalize()





class Seguimiento(models.Model):
    id_seg = models.SmallAutoField(primary_key=True)
    id_gestor = models.ForeignKey(GestorCaso, models.DO_NOTHING, db_column='id_gestor', blank=True, null=True)
    fecharegistro = models.DateField(db_column='fechare', blank=True, null=True)
    descripcion = models.TextField(default='escriba')
    
    def __str__(self):
        return f'{self.id_seg}'
    def clean(self):
       self.descripcion=self.descripcion.capitalize()
    


class Terapia(models.Model):
    id_terapia = models.AutoField(primary_key=True)
    nombreterapia = models.CharField(db_column='nombreTerapia', max_length=40)  # Field name made lowercase.
    def __str__(self):
        return f'{self.nombreterapia}'
    def clean(self):
        self.nombreterapia=self.nombreterapia.capitalize()



class TipReq(models.Model):
    id_req = models.AutoField(primary_key=True)
    nombrerequerimiento = models.CharField(db_column='nombreRequerimiento', max_length=40)  # Field name made lowercase.
    def __str__(self):
        return f'{self.nombrerequerimiento}'

    def clean(self):
        self.nombrerequerimiento=self.nombrerequerimiento.capitalize()


class TipoEnfermedad(models.Model):
    id_enfermedad = models.SmallAutoField(primary_key=True)
    nombreenfermedad = models.CharField(db_column='nombreEnfermedad', max_length=40)  # Field name made lowercase.


    def __str__(self):
        return f'{self.nombreenfermedad}'
    def clean(self):
        self.nombreenfermedad=self.nombreenfermedad.capitalize()



