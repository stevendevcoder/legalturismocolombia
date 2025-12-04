from django.db import models
from .propina import RegistroPropina

class CardServicioVenta(models.Model):
    class CategoriaServicio(models.TextChoices):
        GUIA = "GUIA"
        TRANSPORTE = "TRANSPORTE"
        AVENTURA = "AVENTURA"
        OTRO = "OTRO"

    titulo_card = models.CharField(max_length=150)
    descripcion_corta = models.TextField()
    url_imagen_principal = models.CharField(max_length=255)
    unidad_precio = models.CharField(max_length=50)
    nombre_servicio = models.CharField(max_length=50)
    estado_publicacion = models.BooleanField(default=True)
    categoria_servicio = models.CharField(max_length=20, choices=CategoriaServicio.choices)

    id_registro_propina = models.ForeignKey(
        RegistroPropina, on_delete=models.SET_NULL, null=True
    )
