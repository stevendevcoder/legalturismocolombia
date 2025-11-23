from django.db import models
from .usuario import Usuario

class Rol(models.Model):
    """
    Modelo para gestionar los roles de los usuarios.
    """
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    usuarios = models.ManyToManyField(Usuario, related_name='roles')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
