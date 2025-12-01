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

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateTimeField()
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=250)
    numero_telefonico = models.CharField(max_length=20)
    tipo_identificacion = models.CharField(max_length=50)
    num_identificacion = models.CharField(max_length=50, unique=True)
    url_foto_documento = models.CharField(max_length=255)
    nombre_tipo = models.CharField(max_length=30, choices=TipoUsuario.choices)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.email
