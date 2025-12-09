from django.db import models

class Certificado(models.Model):
    nombre_certificado = models.CharField(max_length=100)
    tipo_certificado = models.CharField(max_length=100)
    entidad_emisora = models.CharField(max_length=100)
    num_registro = models.CharField(max_length=50, unique=True)
    fecha_expedicion = models.DateField(null=True, blank=True)
    url_documento_vigente = models.URLField(max_length=255)

    def __str__(self):
        return self.nombre_certificado

    class Meta:
        verbose_name = "Certificado de Habilidades"
        verbose_name_plural = "Certificados de Habilidades"