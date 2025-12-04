from django.core.exceptions import ObjectDoesNotExist
from ..models.propina import RegistroPropina


class RegistroPropinaRepository:

    # ---------------------------- CREAR ----------------------------
    def create(self, valor_propina):
        """
        Crea un registro de propina.
        valor_propina debe ser uno de los valores definidos en RegistroPropina.ValorPropina.
        """
        propina = RegistroPropina.objects.create(
            valor_propina=valor_propina
        )
        return propina

    # ---------------------------- OBTENER ----------------------------
    def get_by_id(self, propina_id):
        try:
            return RegistroPropina.objects.get(id=propina_id)
        except ObjectDoesNotExist:
            return None

    def get_all(self):
        return RegistroPropina.objects.all()

    # ---------------------------- ACTUALIZAR ----------------------------
    def update(self, propina_id, **kwargs):
        try:
            propina = RegistroPropina.objects.get(id=propina_id)
            for key, value in kwargs.items():
                setattr(propina, key, value)
            propina.save()
            return propina
        except ObjectDoesNotExist:
            return None

    # ---------------------------- ELIMINAR ----------------------------
    def delete(self, propina_id):
        """
        Retorna:
        - True → eliminado
        - False → no existe
        """
        try:
            propina = RegistroPropina.objects.get(id=propina_id)
            propina.delete()
            return True
        except ObjectDoesNotExist:
            return False

    # ---------------------------- CONSULTAS EXTRA ----------------------------
    def get_by_valor(self, valor):
        """
        Filtra todas las propinas que coincidan con un valor específico.
        Ejemplo:
        repo.get_by_valor("10%")
        """
        return RegistroPropina.objects.filter(valor_propina=valor)

    def get_mayores_a(self, porcentajes):
        """
        Retorna todas las propinas cuyo valor esté en la lista dada.
        Útil si amplías los valores en el futuro.
        """
        return RegistroPropina.objects.filter(valor_propina__in=porcentajes)
