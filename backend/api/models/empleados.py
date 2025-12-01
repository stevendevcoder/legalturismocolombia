from django.db import models
from .usuario import Usuario
from .prestador import EmpresaPrestadora
from .certificados import CertificadoHabilidades

class EmpleadoRegistrado(models.Model):
    cargo = models.CharField(max_length=50)
    nit_empresa_fk = models.ForeignKey(EmpresaPrestadora, on_delete=models.CASCADE, related_name='empleados')
    id_usuario_fk = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='empleado_perfil')
    id_certificados_fk = models.ForeignKey(CertificadoHabilidades, on_delete=models.CASCADE, related_name='empleados')

    def __str__(self):
        return f"{self.id_usuario_fk.username} - {self.cargo}"

    class Meta:
        verbose_name = "Empleado Registrado"
        verbose_name_plural = "Empleados Registrados"