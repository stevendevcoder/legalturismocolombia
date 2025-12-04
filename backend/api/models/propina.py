from django.db import models

class RegistroPropina(models.Model):
    class ValorPropina(models.TextChoices):
        BAJO = "10%"
        MEDIO = "20%"
        ALTO = "30%"

    valor_propina = models.CharField(max_length=20, choices=ValorPropina.choices)
