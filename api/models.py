from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField
from django.forms import model_to_dict
# se emigra todas las tablas y se convierten en modelos de clase como una plantilla
class Analista(models.Model):
    analista_id = models.SmallAutoField(primary_key=True)
    id_datos_us = models.ForeignKey('DatosUsuario', models.DO_NOTHING, db_column='id_datos_us')
    id_correo = models.ForeignKey('MensajesCorreo', models.DO_NOTHING, db_column='id_correo')

 





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
    fechaatencioneps = models.DateTimeField(db_column='fechaAtencionEps')  # Field name made lowercase.
    descripcioncaso = models.TextField(db_column='descripcionCaso')  # Field name made lowercase.
  
    estado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='estado')
    fecharesgistrocaso = models.DateTimeField(db_column='fechaResgistroCaso', blank=True,
                                              null=True)  # Field name made lowercase.
    enfermedad = models.ForeignKey('TipoEnfermedad', models.DO_NOTHING, db_column='enfermedad', blank=True)
    fechaatenproceso = models.DateTimeField(db_column='fechaAtenProceso',
                                            null=True)  # Field name made lowercase.
    fechaatenfinalizado = models.DateTimeField(db_column='fechaAtenFinalizado', 
                                               null=True)  # Field name made lowercase.
    fechaatenabierto = models.DateTimeField(db_column='fechaAtenAbierto', 
                                            null=True)  # Field name made lowercase.
    hora = models.TimeField( null=True)
    formula_medica = models.FileField(upload_to='%Y/%m/%d/')

    adjunto_seg = models.FileField(upload_to='%Y/%m/%d/')
    adjunto_terc = models.FileField(upload_to='%Y/%m/%d/')
    id_comple_info = models.OneToOneField('InfoComplementaria', models.DO_NOTHING, db_column='id_comple_info', blank=True,
                                       null=True)
    id_seguimiento = models.OneToOneField('Seguimiento', models.DO_NOTHING, db_column='id_seguimiento')
    id_barrera = models.ForeignKey(BarreraAcceso, models.DO_NOTHING, db_column='id_barrera')
    class Estado_activo(models.TextChoices):
        activo='1',_('activo')
        inactivo='0',_('inactivo')
    estado_pendiente=models.CharField(max_length=8,choices=Estado_activo.choices,default=Estado_activo.activo)
    




class ClasificacionPbs(models.Model):
    id_pbs = models.AutoField(primary_key=True)
    nombrepbs = models.CharField(db_column='nombrePbs', max_length=60)  # Field name made lowercase.
    def __str__(self):
        return f'{self.nombrepbs}'




class DatosAnalisis(models.Model):
    id_analista = models.ForeignKey(Analista, models.DO_NOTHING, db_column='id_analista')
    id_caso = models.ForeignKey(Casos, models.DO_NOTHING, db_column='id_caso', blank=True, null=True)
    informe = models.SmallIntegerField(blank=True, null=True)

    


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

 


class Eps(models.Model):
    cod_eps = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15, blank=True, null=True)

    
    def __str__(self):
        return f'{self.cod_eps} {self.nombre}'


class EspecialidadMed(models.Model):
    id_esp = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    def __str__(self):
        return f'{self.nombre}'




class Estado(models.Model):
    idestado = models.AutoField(db_column='idEstado', primary_key=True)  # Field name made lowercase.
    nombreestado = models.CharField(db_column='nombreEstado', max_length=15)  # Field name made lowercase.
    
    def __str__(self):
        return f'{self.nombreestado}'

   


class Genero(models.Model):
    idgenero = models.PositiveIntegerField(db_column='idGenero', primary_key=True)  # Field name made lowercase.
    nombregenero = models.CharField(db_column='nombreGenero', max_length=5)  # Field name made lowercase.

  
    def __str__(self):
        return f'{self.idgenero} - {self.nombregenero}'


class GestorCaso(models.Model):
    id_gest = models.SmallAutoField(db_column='Id_gest', primary_key=True)  # Field name made lowercase.
    cantcasos = models.SmallIntegerField(db_column='cantCasos', blank=True, null=True)  # Field name made lowercase.
    id_datos_us = models.ForeignKey(DatosUsuario, models.DO_NOTHING, db_column='id_datos_us', blank=True, null=True)
    id_correo = models.ForeignKey('MensajesCorreo', models.DO_NOTHING, db_column='id_correo', blank=True, null=True)

    def __str__(self):
        return f'{self.id_datos_us.primer_nombre}'
    
    
class AsignacionTarea(models.Model):
    id_gest = models.ForeignKey(GestorCaso, models.DO_NOTHING, db_column='id_gest', blank=True, null=True)
    actividad = models.CharField(max_length=40, blank=True, null=True)
    detalle= models.TextField(db_column='detalle',default='')
    fecha = models.DateTimeField()
    fech_registro = models.DateTimeField()
    color = models.CharField(max_length=7, default="#FFFFFF")

    def toJSON(self):
        item = model_to_dict(self)
        return item
class GestorFarmacia(models.Model):
    id_far = models.AutoField(primary_key=True)
    nombrefarmacia = models.CharField(db_column='nombreFarmacia', max_length=40)  # Field name made lowercase.
    def __str__(self):
        return f'{self.nombrefarmacia}'




class GrupoEtnico(models.Model):
    id_gr_etn = models.PositiveIntegerField(primary_key=True)
    nombreetnico = models.CharField(db_column='nombreEtnico', max_length=40)  # Field name made lowercase.

    
    def __str__(self) -> str:
        return f'{self.nombreetnico}'


class IndicadoresGestion(models.Model):
    id_ind_ges = models.PositiveSmallIntegerField()
    idusuario = models.ForeignKey(DatosUsuario, models.DO_NOTHING, db_column='idUsuario')  # Field name made lowercase.
    tiempores = models.DateField(db_column='tiempoRes', blank=True, null=True)  # Field name made lowercase.
    resolutividad = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

   


class InfoComplementaria(models.Model):
    id_comple = models.SmallAutoField(primary_key=True)
    gestor_farma = models.ForeignKey(GestorFarmacia, models.DO_NOTHING, db_column='gestor_farma')
    terapia = models.ForeignKey('Terapia', models.DO_NOTHING, db_column='terapia')
    otra_terapia = models.CharField(max_length=50, blank=True, null=True)
    tipo_req = models.ForeignKey('TipReq', models.DO_NOTHING, db_column='tipo_req', blank=True, null=True)
    clasificacion_pbs = models.ForeignKey(ClasificacionPbs, models.DO_NOTHING ,blank=True, null=True)
    medico_trat = models.CharField(max_length=40)
    especialidad_med = models.ForeignKey(EspecialidadMed, models.DO_NOTHING, db_column='especialidad_med')
    segunda_barrera = models.CharField(max_length=40)
    fech_rad_for_eps = models.DateTimeField(db_column='fech_rad_for_EPS')  # Field name made lowercase.
    fecha_for_medi = models.DateTimeField()
    fecha_aut = models.DateTimeField()
    fech_rad_aut_farm = models.DateTimeField()
    fecha_entrega = models.DateTimeField()
    origen_soli = models.CharField(max_length=40)
    ips_id_terapia = models.ForeignKey('Ips', models.DO_NOTHING, db_column='ips_id_terapia')
    def __str__(self):
        return f'{self.id_comple}'

    


class Ips(models.Model):
    id_terapia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    def __str__(self):
        return f'{self.nombre}'

  


class MensajesCorreo(models.Model):
    id_correo = models.SmallAutoField(primary_key=True)
    recibido = models.TextField(blank=True, null=True)
    enviados = models.CharField(max_length=40, blank=True, null=True)
    asunto = models.CharField(max_length=50, blank=True, null=True)
    mensaje = models.TextField(blank=True, null=True)
    adjunto = models.FileField(upload_to='uploads/% Y/% m/% d/')



class Municipio(models.Model):
    cod_municipio = models.PositiveSmallIntegerField(primary_key=True)
    nombremunicipio = models.CharField(db_column='nombreMunicipio', max_length=15, blank=True,
                                       null=True)  # Field name made lowercase.
   


    def __str__(self):
        return f'{self.cod_municipio} {self.nombremunicipio}'


class PacienteUsuario(models.Model):
    id_paciente = models.SmallAutoField(primary_key=True)
    numusu = models.SmallIntegerField(db_column='numUsu', blank=True, null=True)  # Field name made lowercase.
    id_dat_us = models.ForeignKey(DatosUsuario, models.DO_NOTHING, db_column='id_dat_us', blank=True, null=True)
    id_correo = models.ForeignKey(MensajesCorreo, models.DO_NOTHING, db_column='id_correo', blank=True, null=True)




class Pais(models.Model):
    cod_pais = models.SmallAutoField(primary_key=True)
    nombrepais = models.CharField(db_column='nombrePais', max_length=40)  # Field name made lowercase.


    def __str__(self) -> str:
        ""
        ""
        return f'{self.cod_pais} {self.nombrepais}'


class PoblacionEspecial(models.Model):
    id_pb_esp = models.PositiveIntegerField(primary_key=True)
    nombrepoblacionesp = models.CharField(db_column='nombrePoblacionEsp', max_length=40, blank=True,
                                          null=True)  # Field name made lowercase.


    
    def __str__(self)->str:
        return f'{self.id_pb_esp} {self.nombrepoblacionesp}'


class Regimen(models.Model):
    cod_regimen = models.PositiveIntegerField(primary_key=True)
    nombreregimen = models.CharField(db_column='nombreRegimen', max_length=15)  # Field name made lowercase.

 
    def __str__(self):
        return f'{self.cod_regimen} - {self.nombreregimen}'


class TipoDocumento(models.Model):
    id_doc = models.AutoField(primary_key=True)
    nombredocumento = models.CharField(db_column='nombreDocumento', max_length=40)  # Field name made lowercase.

 

    def __str__(self):
        return f'{self.nombredocumento}'


class Reportes(models.Model):
    id_caso = models.ForeignKey(Casos, models.DO_NOTHING, db_column='id_caso')
    reporte = models.FileField(upload_to='uploads/% Y/% m/% d/')





class Seguimiento(models.Model):
    id_seg = models.SmallAutoField(primary_key=True)
    id_gestor = models.ForeignKey(GestorCaso, models.DO_NOTHING, db_column='id_gestor')
    fecharegistro = models.DateField(db_column='fechare', blank=True, null=True)
    descripcion = models.TextField()
    
    def __str__(self):
        return f'{self.id_seg}'

    


class Terapia(models.Model):
    id_terapia = models.AutoField(primary_key=True)
    nombreterapia = models.CharField(db_column='nombreTerapia', max_length=40)  # Field name made lowercase.
    def __str__(self):
        return f'{self.nombreterapia}'




class TipReq(models.Model):
    id_req = models.AutoField(primary_key=True)
    nombrerequerimiento = models.CharField(db_column='nombreRequerimiento', max_length=40)  # Field name made lowercase.
    def __str__(self):
        return f'{self.nombrerequerimiento}'




class TipoEnfermedad(models.Model):
    id_enfermedad = models.SmallAutoField(primary_key=True)
    nombreenfermedad = models.CharField(db_column='nombreEnfermedad', max_length=40)  # Field name made lowercase.


    def __str__(self):
        return f'{self.nombreenfermedad}'


class VisualizacionCasoHistorial(models.Model):
    idcaso = models.ForeignKey(Casos, models.DO_NOTHING, db_column='idCaso')  # Field name made lowercase.
    estado_caso = models.CharField(max_length=40, blank=True, null=True)
    id_usuario = models.ForeignKey(DatosUsuario, models.DO_NOTHING, db_column='id_usuario')



    def __str__(self):
        return f'id caso: {self.idcaso} estado caso{self.estado_caso} id_usuario {self.id_usuario}'
