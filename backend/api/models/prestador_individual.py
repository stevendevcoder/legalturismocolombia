from django.db import models
from django.conf import settings
from .certificados import Certificado
from .servicio import CardServicioVenta

class PrestadorIndividual(models.Model):
    profesion_servicio_principal = models.CharField(max_length=100)
    estado_afiliacion_seguridad = models.BooleanField(default=False)
    url_rut = models.CharField(max_length=255)
    matricula_comerciante_ind = models.CharField(max_length=50)
    municipio_operacion = models.CharField(max_length=100)
    lugar_prestacion_servicio = models.CharField(max_length=100)
    url_permiso_alcaldia = models.CharField(max_length=255)

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='prestador_individual')
    card_servicio = models.ForeignKey(CardServicioVenta, on_delete=models.SET_NULL, null=True, blank=True)
    certificado = models.ForeignKey(Certificado, on_delete=models.SET_NULL, null=True, blank=True)