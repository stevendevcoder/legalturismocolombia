from django.db import models
from django.conf import settings # Best practice para referenciar al usuario

class Turista(models.Model):
    # Cambié 'id_usuario' por 'usuario' para ser más pythonico
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='perfil_turista'
    )
    pais_residencia = models.CharField(max_length=100)
    idioma_preferido = models.CharField(max_length=100)
    contacto_emergencia_nombre = models.CharField(max_length=150)
    contacto_emergencia_telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"Turista: {self.usuario.email}"