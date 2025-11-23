from django.db import models
from .usuario import Usuario
from .prestador import PrestadorServicio

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
    estado = models.CharField(max_length=50, default='pendiente')

    def __str__(self):
        return f"Denuncia de {self.usuario} a {self.prestador}"

    class Meta:
        verbose_name = "Denuncia"
        verbose_name_plural = "Denuncias"
