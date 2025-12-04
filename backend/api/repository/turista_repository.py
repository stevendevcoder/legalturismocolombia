from django.core.exceptions import ObjectDoesNotExist
from ..models.turista import Turista


class TuristaRepository:

    # ---------------------------- CREAR ----------------------------
    def create(
        self,
        pais_residencia,
        idioma_preferido,
        contacto_emergencia_nombre,
        contacto_emergencia_telefono,
        id_usuario
    ):
        turista = Turista.objects.create(
            pais_residencia=pais_residencia,
            idioma_preferido=idioma_preferido,
            contacto_emergencia_nombre=contacto_emergencia_nombre,
            contacto_emergencia_telefono=contacto_emergencia_telefono,
            id_usuario=id_usuario
        )
        return turista

    # ---------------------------- OBTENER ----------------------------
    def get_by_id(self, turista_id):
        try:
            return Turista.objects.get(id=turista_id)
        except ObjectDoesNotExist:
            return None

    def get_all(self):
        return Turista.objects.all()

    def get_by_usuario(self, usuario_id):
        """Obtiene un turista según el usuario asociado. (OneToOne)"""
        try:
            return Turista.objects.get(id_usuario__id=usuario_id)
        except ObjectDoesNotExist:
            return None

    # ---------------------------- ACTUALIZAR ----------------------------
    def update(self, turista_id, **kwargs):
        try:
            turista = Turista.objects.get(id=turista_id)
            for key, value in kwargs.items():
                setattr(turista, key, value)
            turista.save()
            return turista
        except ObjectDoesNotExist:
            return None

    # ---------------------------- ELIMINAR ----------------------------
    def delete(self, turista_id):
        try:
            turista = Turista.objects.get(id=turista_id)
            turista.delete()
            return True
        except ObjectDoesNotExist:
            return False

    # ---------------------------- CONSULTAS EXTRA ----------------------------
    def get_by_pais(self, pais):
        """Filtra turistas por país de residencia."""
        return Turista.objects.filter(pais_residencia=pais)

    def search_by_idioma(self, idioma):
        """Busca turistas por coincidencia parcial en el idioma preferido."""
        return Turista.objects.filter(idioma_preferido__icontains=idioma)

    def get_by_contacto_emergencia(self, nombre):
        """Filtra turistas por el nombre del contacto de emergencia."""
        return Turista.objects.filter(
            contacto_emergencia_nombre__icontains=nombre
        )
