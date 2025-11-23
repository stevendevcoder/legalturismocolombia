from django.db import models
from .usuario import Usuario

class PrestadorServicio(models.Model):
    """
    Modelo para los prestadores de servicios turísticos.
    """
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='prestador_perfil')
    nombre_empresa = models.CharField(max_length=255)
    rnt = models.CharField(max_length=50, unique=True, verbose_name="Registro Nacional de Turismo")
    descripcion = models.TextField()
    validado = models.BooleanField(default=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_empresa

    class Meta:
        verbose_name = "Prestador de Servicio"
        verbose_name_plural = "Prestadores de Servicios"
