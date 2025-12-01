from django.db import models
from .usuario import Usuario

class EmpresaPrestadora(models.Model):
    nit_empresa = models.CharField(max_length=50, primary_key=True)
    nombre_razon_social = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    barrio = models.CharField(max_length=200)
    categoria_empresa = models.CharField(
        max_length=50,
        choices=[
            ('hotel', 'Hotel'),
            ('restaurante', 'Restaurante'),
            ('transporte', 'Transporte'),
            ('guia', 'Guía Turístico'),
            ('otro', 'Otro'),
        ]
    )
    rnt_empresa = models.CharField(max_length=50, unique=True)
    url_rnt_certificado = models.URLField(max_length=255)
    matricula_mercantil = models.CharField(max_length=50)
    url_cert_camara_comercio = models.URLField(max_length=255)
    url_cert_bomberos = models.URLField(max_length=255)
    url_cert_uso_suelo = models.URLField(max_length=255)
    id_representante_fk = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='empresas_representadas')
    id_cardServicioVenta_fk = models.ForeignKey('ServicioTuristico', on_delete=models.CASCADE, blank=True, null=True, related_name='empresa_principal')
    id_certificadosHabilidades_fk = models.ForeignKey('CertificadoHabilidades', on_delete=models.CASCADE, blank=True, null=True, related_name='empresa_principal')

    def __str__(self):
        return self.nombre_razon_social

    class Meta:
        verbose_name = "Empresa Prestadora"
        verbose_name_plural = "Empresas Prestadoras"


class PrestadorIndividual(models.Model):
    """
    Modelo para prestadores individuales de servicios turísticos.
    """
    profesion_servicio_principal = models.CharField(max_length=100)
    estado_afiliacion_seguridad = models.BooleanField()
    url_rut = models.URLField(max_length=255)
    matricula_comerciante_ind = models.CharField(max_length=50)
    municipio_operacion = models.CharField(max_length=100)
    lugar_prestacion_servicio = models.CharField(max_length=100)
    url_permiso_alcaldia = models.URLField(max_length=255)
    id_usuario_fk = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='prestador_individual')
    id_certificados_habilidades_fk = models.ForeignKey('CertificadoHabilidades', on_delete=models.CASCADE, related_name='prestador_individual')
    id_cardServicioVenta_fk = models.ForeignKey('ServicioTuristico', on_delete=models.CASCADE, blank=True, null=True, related_name='prestador_individual_principal')

    def __str__(self):
        return f"{self.id_usuario_fk.username} - Prestador Individual"

    class Meta:
        verbose_name = "Prestador Individual"
        verbose_name_plural = "Prestadores Individuales"
