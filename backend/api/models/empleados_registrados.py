from django.db import models
from .usuario import Usuario
from .empresas_prestadoras import EmpresaPrestadora
from .certificados import CertificadoHabilidad

class EmpleadoRegistrado(models.Model):
    cargo = models.CharField(max_length=50)
    nit_empresa_fk = models.ForeignKey(EmpresaPrestadora, on_delete=models.CASCADE)
    id_usuario_fk = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_certificados = models.ForeignKey(
        CertificadoHabilidad, on_delete=models.SET_NULL, null=True
    )
