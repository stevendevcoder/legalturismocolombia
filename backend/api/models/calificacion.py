from django.db import models
from .usuario import Usuario
from .prestador import PrestadorServicio

class Calificacion(models.Model):
    """
    Modelo para calificaciones y comentarios.
    """
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='calificaciones')
    puntuacion = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Calificación {self.puntuacion} de {self.usuario}"

    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"
