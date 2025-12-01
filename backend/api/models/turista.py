from django.db import models
from .usuario import Usuario

class Turista(models.Model):
    pais_residencia = models.CharField(max_length=100)
    idioma_preferido = models.CharField(max_length=100)
    contacto_emergencia_nombre = models.CharField(max_length=150)
    contacto_emergencia_telefono = models.CharField(max_length=20)
    id_usuarios_fk = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='turista_perfil')

    def __str__(self):
        return f"{self.id_usuarios_fk.username} - Turista"

    class Meta:
        verbose_name = "Turista"
        verbose_name_plural = "Turistas"