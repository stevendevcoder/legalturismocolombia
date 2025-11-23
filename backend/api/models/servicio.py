from django.db import models
from .prestador import PrestadorServicio

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

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Servicio Turístico"
        verbose_name_plural = "Servicios Turísticos"
