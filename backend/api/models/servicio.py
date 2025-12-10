from django.db import models
from .prestador import PrestadorServicio
from django.db.models import Avg


class ServicioTuristico(models.Model):
    """
    Modelo para los servicios turísticos ofrecidos.
    """
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='servicios')
    nombre = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    certificado = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    def promedio_calificacion(self):
        reseñas = self.reseñas.all()
        if reseñas.exists():
            return sum(r.estrellas for r in reseñas) / reseñas.count()
        return 0
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Servicio Turístico"
        verbose_name_plural = "Servicios Turísticos"
    
    
    

    