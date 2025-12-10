from django.db import models
from django.conf import settings
from .certificados import Certificado
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
    
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='empresa_prestadora')
    card_servicio = models.ForeignKey(CardServicioVenta, on_delete=models.SET_NULL, null=True, blank=True)
    certificado = models.ForeignKey(Certificado, on_delete=models.SET_NULL, null=True, blank=True)
