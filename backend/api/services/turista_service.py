from api.models import Turista, Usuario

class TuristaRepository:
    @staticmethod
    def get_all():
        return Turista.objects.all()

    @staticmethod
    def get_by_id(turista_id):
        return Turista.objects.filter(id=turista_id).first()

    @staticmethod
    def create(data):
        usuario_data = data.pop('id_usuarios_fk')
        usuario = Usuario.objects.create(**usuario_data)
        turista = Turista.objects.create(id_usuarios_fk=usuario, **data)
        return turista

    @staticmethod
    def update(turista_id, data):
        turista = TuristaRepository.get_by_id(turista_id)
        if not turista:
            return None
        usuario_data = data.pop('id_usuarios_fk', {})
        usuario = turista.id_usuarios_fk
        for attr, value in usuario_data.items():
            setattr(usuario, attr, value)
        usuario.save()
        for attr, value in data.items():
            setattr(turista, attr, value)
        turista.save()
        return turista

    @staticmethod
    def delete(turista_id):
        turista = TuristaRepository.get_by_id(turista_id)
        if turista:
            usuario = turista.id_usuarios_fk
            turista.delete()
            usuario.delete()
            return True
        return False

class TuristaService:
    @staticmethod
    def listar_turistas():
        return TuristaRepository.get_all()

    @staticmethod
    def obtener_turista(turista_id):
        return TuristaRepository.get_by_id(turista_id)

    @staticmethod
    def crear_turista(data):
        return TuristaRepository.create(data)

    @staticmethod
    def actualizar_turista(turista_id, data):
        return TuristaRepository.update(turista_id, data)

    @staticmethod
    def eliminar_turista(turista_id):
        return TuristaRepository.delete(turista_id)