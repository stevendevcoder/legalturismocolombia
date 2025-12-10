from django.db import models
from .usuario import Usuario
from .empresas_prestadoras import EmpresaPrestadora
from .certificados import Certificado

class EmpleadoRegistrado(models.Model):
    cargo = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    nit_empresa_fk = models.ForeignKey(EmpresaPrestadora, on_delete=models.CASCADE)
    id_usuario_fk = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_certificados = models.ForeignKey(
        Certificado, on_delete=models.SET_NULL, null=True
    )
