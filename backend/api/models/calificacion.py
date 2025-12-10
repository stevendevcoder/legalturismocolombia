from django.db import models
from .servicio import CardServicioVenta
from .turista import Turista

class CalificacionServicioUsuario(models.Model):
    class Escala(models.TextChoices):
        UNO = "1"
        DOS = "2"
        TRES = "3"
        CUATRO = "4"
        CINCO = "5"

    puntuacion_general = models.CharField(max_length=2, choices=Escala.choices)
    feedback_empresa = models.CharField(max_length=50)
    puntuacion_certificados = models.CharField(max_length=2, choices=Escala.choices)
    calificacion_puntualidad = models.CharField(max_length=2, choices=Escala.choices)
    calificacion_limpieza = models.CharField(max_length=2, choices=Escala.choices)
    fecha_calificacion = models.DateTimeField(null=True, blank=True)
    id_card_servicio = models.ForeignKey(CardServicioVenta, on_delete=models.CASCADE)
    id_turistas = models.ForeignKey(Turista, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    
    def __str__(self):
        return f"Calificación {self.puntuacion} de {self.usuario}"

    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"
        
   
    
