from django.db import models
from .prestador import EmpresaPrestadora, PrestadorIndividual
from .propina import RegistroPropina

class ServicioTuristico(models.Model):
    titulo_card = models.CharField(max_length=150)
    descripcion_corta = models.TextField()
    url_imagen_principal = models.URLField(max_length=255)
    unidad_precio = models.CharField(max_length=50)
    nombre_servicio = models.CharField(max_length=50)
    categoria_servicio = models.CharField(
        max_length=50,
        choices=[
            ('hotel', 'Hotel'),
            ('restaurante', 'Restaurante'),
            ('transporte', 'Transporte'),
            ('guia', 'Guía Turístico'),
            ('otro', 'Otro'),
        ]
    )
    id_registro_propina_fk = models.ForeignKey(RegistroPropina, on_delete=models.CASCADE, related_name='servicios')
    # Can be offered by empresa or individual, so add foreign keys
    empresa_prestadora = models.ForeignKey(EmpresaPrestadora, on_delete=models.CASCADE, blank=True, null=True, related_name='servicios')
    prestador_individual = models.ForeignKey(PrestadorIndividual, on_delete=models.CASCADE, blank=True, null=True, related_name='servicios')

    def __str__(self):
        return self.titulo_card

    class Meta:
        verbose_name = "Servicio Turístico"
        verbose_name_plural = "Servicios Turísticos"
