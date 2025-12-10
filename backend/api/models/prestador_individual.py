from django.db import models
from .usuario import Usuario
from .certificados import CertificadoHabilidad
from .servicio import CardServicioVenta

class PrestadorIndividual(models.Model):
    profesion_servicio_principal = models.CharField(max_length=100)
    estado_afiliacion_seguridad = models.BooleanField(default=False)
    url_rut = models.CharField(max_length=255)
    matricula_comerciante_ind = models.CharField(max_length=50)
    municipio_operacion = models.CharField(max_length=100)
    lugar_prestacion_servicio = models.CharField(max_length=100)
    url_permiso_alcaldia = models.CharField(max_length=255)

    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    # Removed id_cardServicioVenta and id_certificadosHabilidades as they are now Reverse Relations (OneToMany)
