from django.db import models
from .usuario import Usuario
from .prestador import EmpresaPrestadora, PrestadorIndividual
from .turista import Turista

class Denuncia(models.Model):
    persona_reportada_tipo = models.CharField(
        max_length=50,
        choices=[
            ('turista', 'Turista'),
            ('prestador_individual', 'Prestador Individual'),
            ('empresa', 'Empresa'),
        ]
    )
    fecha_hora_reporte = models.DateTimeField(auto_now_add=True)
    tipo_reporte = models.CharField(
        max_length=50,
        choices=[
            ('fraude', 'Fraude'),
            ('mal_servicio', 'Mal Servicio'),
            ('ilegal', 'Actividad Ilegal'),
            ('otro', 'Otro'),
        ]
    )
    descripcion_detallada = models.TextField()
    url_evidencia_adjunta = models.URLField(max_length=255, blank=True, null=True)
    estado_gestion = models.CharField(
        max_length=50,
        choices=[
            ('pendiente', 'Pendiente'),
            ('en_revision', 'En Revisión'),
            ('resuelto', 'Resuelto'),
            ('cerrado', 'Cerrado'),
        ],
        default='pendiente'
    )
    fecha_cierre_gestion = models.DateTimeField(blank=True, null=True)
    gestion_tomada = models.TextField(blank=True, null=True)
    id_prestador_individual_reportado_fk = models.ForeignKey(PrestadorIndividual, on_delete=models.CASCADE, blank=True, null=True, related_name='denuncias_recibidas')
    id_empresas_prestadoras_fk = models.ForeignKey(EmpresaPrestadora, on_delete=models.CASCADE, blank=True, null=True, related_name='denuncias_recibidas')
    id_turista_fk = models.ForeignKey(Turista, on_delete=models.CASCADE, blank=True, null=True, related_name='denuncias_recibidas')
    # Assuming the reporter is a Usuario
    reporter = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='denuncias_realizadas')

    def __str__(self):
        return f"Reporte {self.id} - {self.tipo_reporte}"

    class Meta:
        verbose_name = "Denuncia"
        verbose_name_plural = "Denuncias"
