from django.db import models
from .servicio import ServicioTuristico
from .turista import Turista

class Calificacion(models.Model):
    puntuacion_general = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    feedback_empresa = models.CharField(max_length=50, blank=True, null=True)
    puntuacion_certificados = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], blank=True, null=True)
    calificacion_puntualidad = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], blank=True, null=True)
    calificacion_limpieza = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], blank=True, null=True)
    fecha_calificacion = models.DateTimeField(auto_now_add=True)
    id_card_servicio_fk = models.ForeignKey(ServicioTuristico, on_delete=models.CASCADE, related_name='calificaciones')
    id_turistas_fk = models.ForeignKey(Turista, on_delete=models.CASCADE, related_name='calificaciones')

    def __str__(self):
        return f"Calificación {self.puntuacion_general} para {self.id_card_servicio_fk}"

    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"
