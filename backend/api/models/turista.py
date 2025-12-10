from django.db import models
from django.conf import settings

class Turista(models.Model):
    
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
