from django.db import models
from .usuario import Usuario

class Turista(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='turista_perfil')
    nacionalidad = models.CharField(max_length=100, blank=True, null=True)
    numero_pasaporte = models.CharField(max_length=50, unique=True, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - Turista"

    class Meta:
        verbose_name = "Turista"
        verbose_name_plural = "Turistas"