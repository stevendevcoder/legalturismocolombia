from django.db import models

class RegistroPropina(models.Model):
    valor_propina = models.CharField(
        max_length=10,
        choices=[
            ('5%', '5%'),
            ('10%', '10%'),
            ('15%', '15%'),
            ('20%', '20%'),
        ]
    )

    def __str__(self):
        return f"Propina {self.valor_propina}"

    class Meta:
        verbose_name = "Registro de Propina"
        verbose_name_plural = "Registros de Propinas"