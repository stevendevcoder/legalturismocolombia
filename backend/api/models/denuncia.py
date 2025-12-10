from django.db import models
from .prestador_individual import PrestadorIndividual
from .empresas_prestadoras import EmpresaPrestadora
from .turista import Turista

class RegistroReporte(models.Model):
    class TipoReporte(models.TextChoices):
        QUEJA = "QUEJA"
        RECLAMO = "RECLAMO"
        DENUNCIA = "DENUNCIA"
    class EstadoGestion(models.TextChoices):
        ABIERTO = "ABIERTO"
        EN_PROCESO = "EN_PROCESO"
        CERRADO = "CERRADO"

    fecha_hora_reporte = models.DateTimeField(null=True, blank=True)
    tipo_reporte = models.CharField(max_length=20, choices=TipoReporte.choices)
    descripcion_detallada = models.TextField()
    url_evidencia_adjunta = models.CharField(max_length=255, null=True, blank=True)
    estado_gestion = models.CharField(max_length=20, choices=EstadoGestion.choices)
    fecha_cierre_gestion = models.DateTimeField(null=True, blank=True)
    gestion_tomada = models.TextField(null=True, blank=True)

    id_prestador_individual_reportado = models.ForeignKey(
        PrestadorIndividual, on_delete=models.SET_NULL, null=True
    )
    id_empresas_prestadoras = models.ForeignKey(
        EmpresaPrestadora, on_delete=models.SET_NULL, null=True
    )
    id_turista = models.ForeignKey(
        Turista, on_delete=models.SET_NULL, null=True
    )
