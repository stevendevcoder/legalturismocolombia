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
class Denuncia(models.Model):
    """
    Modelo para gestionar las denuncias realizadas por usuarios.
    """
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='denuncias_realizadas')
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='denuncias_recibidas')
    motivo = models.CharField(max_length=255)
    descripcion = models.TextField()
    evidencia = models.FileField(upload_to='evidencias/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=[('pendiente', 'Pendiente'), ('resuelta', 'Resuelta')],
        default='pendiente'
    )

    fecha_hora_reporte = models.DateTimeField(null=True, blank=True)
    tipo_reporte = models.CharField(max_length=20, choices=TipoReporte.choices)
    descripcion_detallada = models.TextField()
    url_evidencia_adjunta = models.CharField(max_length=255, null=True, blank=True)
    estado_gestion = models.CharField(max_length=20, choices=EstadoGestion.choices)
    fecha_cierre_gestion = models.DateTimeField(null=True, blank=True)
    gestion_tomada = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Denuncia"
        verbose_name_plural = "Denuncias"
    
    
