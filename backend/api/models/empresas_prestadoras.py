from django.db import models
from .usuario import Usuario
from .certificados import CertificadoHabilidad
from .servicio import CardServicioVenta

class EmpresaPrestadora(models.Model):
    class Categoria(models.TextChoices):
        A = "Culural"
        B = "Natural"
        C = "Histórico"
        D = "Recreacional"
        E = "Gastronómico"
        F = "Otros"

    nit_empresa = models.CharField(primary_key=True, max_length=50)
    nombre_razon_social = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    categoria_empresa = models.CharField(max_length=20, choices=Categoria.choices)
    rnt_empresa = models.CharField(max_length=50, unique=True)
    url_rnt_certificado = models.CharField(max_length=255)
    matricula_mercantil = models.CharField(max_length=50)
    url_cert_camara_comercio = models.CharField(max_length=255)

    id_usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE
    )
    id_cardServicioVenta = models.ForeignKey(
        CardServicioVenta, on_delete=models.SET_NULL, null=True
    )
    id_certificadosHabilidades = models.ForeignKey(
        CertificadoHabilidad, on_delete=models.SET_NULL, null=True
    )
