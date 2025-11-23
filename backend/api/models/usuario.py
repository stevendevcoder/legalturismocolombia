from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    """
    Modelo personalizado de usuario.
    """
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
