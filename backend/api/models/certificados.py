from django.db import models

# Avoid circular imports by using strings for models
class CertificadoHabilidad(models.Model):
    nombre_certificado = models.CharField(max_length=100)
    tipo_certificado = models.CharField(max_length=100)
    entidad_emisora = models.CharField(max_length=100)
    num_registro = models.CharField(max_length=50, unique=True)
    fecha_expedicion = models.DateField()
    url_documento_vigente = models.URLField(max_length=255)
    
    # Relations
    empresa_prestadora = models.ForeignKey('EmpresaPrestadora', on_delete=models.CASCADE, null=True, blank=True, related_name='certificados')
    prestador_individual = models.ForeignKey('PrestadorIndividual', on_delete=models.CASCADE, null=True, blank=True, related_name='certificados')

    def __str__(self):
        return self.nombre_certificado

    class Meta:
        verbose_name = "Certificado de Habilidad"
        verbose_name_plural = "Certificados de Habilidades"