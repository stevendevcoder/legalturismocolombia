from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UsuarioManager

class Usuario(AbstractBaseUser, PermissionsMixin):
    class TipoUsuario(models.TextChoices):
        TURISTA = "TURISTA", "Turista"
        PRESTADOR = "PRESTADOR", "Prestador Individual"
        EMPRESA = "EMPRESA", "Empresa"

    username = None # Desactivamos username por defecto
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    numero_telefonico = models.CharField(max_length=20)
    tipo_identificacion = models.CharField(max_length=50)
    num_identificacion = models.CharField(max_length=50, unique=True)
    url_foto_documento = models.CharField(max_length=255, blank=True, null=True)
    nombre_tipo = models.CharField(max_length=30, choices=TipoUsuario.choices)
    activo = models.BooleanField(default=True)
    
    # Staff status es necesario para el admin de Django
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    objects = UsuarioManager()

    def __str__(self):
        return self.email