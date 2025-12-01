from django.db import models

class CertificadoHabilidades(models.Model):
    nombre_certificado = models.CharField(max_length=100)
    tipo_certificado = models.CharField(max_length=100)
    entidad_emisora = models.CharField(max_length=100)
    num_registro_o_tarjeta = models.CharField(max_length=50, unique=True)
    fecha_expedicion = models.DateField()
    fecha_vencimiento = models.DateField()
    url_documento_vigente = models.URLField(max_length=255)

    def __str__(self):
        return self.nombre_certificado

    class Meta:
        verbose_name = "Certificado de Habilidades"
        verbose_name_plural = "Certificados de Habilidades"