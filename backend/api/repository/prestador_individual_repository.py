from django.core.exceptions import ObjectDoesNotExist
from ..models.prestador_individual import PrestadorIndividual


class PrestadorIndividualRepository:

    # ---------------------------- CREAR ----------------------------
    def create(
        self,
        profesion_servicio_principal,
        estado_afiliacion_seguridad,
        url_rut,
        matricula_comerciante_ind,
        municipio_operacion,
        lugar_prestacion_servicio,
        url_permiso_alcaldia,
        id_usuario,
        id_certificados_habilidades=None,
        id_cardServicioVenta=None
    ):
        prestador = PrestadorIndividual.objects.create(
            profesion_servicio_principal=profesion_servicio_principal,
            estado_afiliacion_seguridad=estado_afiliacion_seguridad,
            url_rut=url_rut,
            matricula_comerciante_ind=matricula_comerciante_ind,
            municipio_operacion=municipio_operacion,
            lugar_prestacion_servicio=lugar_prestacion_servicio,
            url_permiso_alcaldia=url_permiso_alcaldia,
            id_usuario=id_usuario,
            id_certificados_habilidades=id_certificados_habilidades,
            id_cardServicioVenta=id_cardServicioVenta
        )
        return prestador

    # ---------------------------- OBTENER ----------------------------
    def get_by_id(self, prestador_id):
        try:
            return PrestadorIndividual.objects.get(id=prestador_id)
        except ObjectDoesNotExist:
            return None

    def get_all(self):
        return PrestadorIndividual.objects.all()

    # ---------------------------- ACTUALIZAR ----------------------------
    def update(self, prestador_id, **kwargs):
        try:
            prestador = PrestadorIndividual.objects.get(id=prestador_id)
            for key, value in kwargs.items():
                setattr(prestador, key, value)
            prestador.save()
            return prestador
        except ObjectDoesNotExist:
            return None

    # ---------------------------- ELIMINAR ----------------------------
    def delete(self, prestador_id):
        """
        Retorna:
        - True → eliminado correctamente
        - False → no existe
        """
        try:
            prestador = PrestadorIndividual.objects.get(id=prestador_id)
            prestador.delete()
            return True
        except ObjectDoesNotExist:
            return False

    # ---------------------------- CONSULTAS EXTRA ----------------------------
    def get_by_usuario(self, usuario_id):
        """Prestadores asociados a un usuario específico."""
        return PrestadorIndividual.objects.filter(id_usuario__id=usuario_id)

    def get_by_municipio(self, municipio):
        """Filtra por municipio de operación."""
        return PrestadorIndividual.objects.filter(municipio_operacion=municipio)

    def get_afiliados(self):
        """Filtra prestadores SÍ afiliados a seguridad social."""
        return PrestadorIndividual.objects.filter(estado_afiliacion_seguridad=True)

    def get_no_afiliados(self):
        """Filtra prestadores NO afiliados a seguridad social."""
        return PrestadorIndividual.objects.filter(estado_afiliacion_seguridad=False)
