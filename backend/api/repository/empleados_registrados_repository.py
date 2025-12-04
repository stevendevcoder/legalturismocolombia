from django.core.exceptions import ObjectDoesNotExist
from ..models.empleados_registrados import EmpleadoRegistrado


class EmpleadoRegistradoRepository:

    # ---------------------------- CREAR ----------------------------
    def create(self, cargo, nit_empresa_fk, id_usuario_fk, id_certificados=None):
        empleado = EmpleadoRegistrado.objects.create(
            cargo=cargo,
            nit_empresa_fk=nit_empresa_fk,
            id_usuario_fk=id_usuario_fk,
            id_certificados=id_certificados
        )
        return empleado

    # ---------------------------- OBTENER ----------------------------
    def get_by_id(self, empleado_id):
        try:
            return EmpleadoRegistrado.objects.get(id=empleado_id)
        except ObjectDoesNotExist:
            return None

    def get_all(self):
        return EmpleadoRegistrado.objects.all()

    # ---------------------------- ACTUALIZAR ----------------------------
    def update(self, empleado_id, **kwargs):
        try:
            empleado = EmpleadoRegistrado.objects.get(id=empleado_id)
            for key, value in kwargs.items():
                setattr(empleado, key, value)
            empleado.save()
            return empleado
        except ObjectDoesNotExist:
            return None

    # ---------------------------- ELIMINAR ----------------------------
    def delete(self, empleado_id):
        try:
            empleado = EmpleadoRegistrado.objects.get(id=empleado_id)
            empleado.delete()
            return True
        except ObjectDoesNotExist:
            return False
