from django.db import models
from .usuario import Usuario
from .prestador import PrestadorServicio

class Interaccion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE)
    fecha_interaccion = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=50, default='reserva') # reserva, visita, etc.

    def __str__(self):
        return f"Interacción {self.usuario} - {self.prestador}"

    class Meta:
        verbose_name = "Interacción"
        verbose_name_plural = "Interacciones"
