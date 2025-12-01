from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):

    fecha_nacimiento = models.DateTimeField(blank=True, null=True)
    numero_telefonico = models.CharField(max_length=20, blank=True, null=True)
    tipo_identificacion = models.CharField(max_length=50, blank=True, null=True)
    num_identificacion = models.CharField(max_length=50, unique=True, blank=True, null=True)
    url_foto_documento = models.URLField(max_length=255, blank=True, null=True)
    nombre_tipo = models.CharField(
        max_length=50,
        choices=[
            ('turista', 'Turista'),
            ('prestador_individual', 'Prestador Individual'),
            ('empresa', 'Empresa'),
            ('admin', 'Administrador'),
        ],
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
