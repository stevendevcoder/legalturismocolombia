from django.db import models
from .propina import RegistroPropina

class CardServicioVenta(models.Model):
    class CategoriaServicio(models.TextChoices):
        HOSPEDAJE = "HOSPEDAJE", "Hospedaje"
        AGENCIAS_TOURS = "AGENCIAS_TOURS", "Agencias y Tours"
        GUIAS = "GUIAS", "Guías"
        TRANSPORTE = "TRANSPORTE", "Transporte"
        AVENTURA_RECREACION = "AVENTURA_RECREACION", "Aventura y Recreación"
        SALUD_BIENESTAR = "SALUD_BIENESTAR", "Salud y Bienestar"
        OTRO = "OTRO", "Otro"

    titulo_card = models.CharField(max_length=150)
    descripcion_corta = models.TextField()
    url_imagen_principal = models.CharField(max_length=255)
    unidad_precio = models.CharField(max_length=50)
    nombre_servicio = models.CharField(max_length=50, null=True, blank=True)
    estado_publicacion = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    categoria_servicio = models.CharField(max_length=50, choices=CategoriaServicio.choices)

    id_registro_propina = models.ForeignKey(
        RegistroPropina, on_delete=models.SET_NULL, null=True
    )
    
    
    empresa_prestadora = models.ForeignKey('EmpresaPrestadora', on_delete=models.CASCADE, null=True, blank=True, related_name='servicios')
    prestador_individual = models.ForeignKey('PrestadorIndividual', on_delete=models.CASCADE, null=True, blank=True, related_name='servicios')

