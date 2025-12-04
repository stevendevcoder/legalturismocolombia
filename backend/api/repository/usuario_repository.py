from django.core.exceptions import ObjectDoesNotExist

from legalturismocolombia.backend.api import models
from ..models.usuario import Usuario


class UsuarioRepository:

    # ---------------------------- CREAR ----------------------------
    def create(
        self,
        nombre,
        apellido,
        fecha_nacimiento,
        email,
        password_hash,
        numero_telefonico,
        tipo_identificacion,
        num_identificacion,
        url_foto_documento,
        nombre_tipo,
        activo=True
    ):
        usuario = Usuario.objects.create(
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            email=email,
            password_hash=password_hash,
            numero_telefonico=numero_telefonico,
            tipo_identificacion=tipo_identificacion,
            num_identificacion=num_identificacion,
            url_foto_documento=url_foto_documento,
            nombre_tipo=nombre_tipo,
            activo=activo
        )
        return usuario

    # ---------------------------- OBTENER ----------------------------
    def get_by_id(self, usuario_id):
        try:
            return Usuario.objects.get(id=usuario_id)
        except ObjectDoesNotExist:
            return None

    def get_all(self):
        return Usuario.objects.all()

    def get_by_email(self, email):
        """Obtiene un usuario por email (útil para login)."""
        try:
            return Usuario.objects.get(email=email)
        except ObjectDoesNotExist:
            return None

    def get_by_identificacion(self, numero):
        """Obtiene un usuario por su número de documento."""
        try:
            return Usuario.objects.get(num_identificacion=numero)
        except ObjectDoesNotExist:
            return None

    def get_by_tipo(self, tipo):
        """Filtra usuarios por tipo (TURISTA, EMPRESA, etc)."""
        return Usuario.objects.filter(nombre_tipo=tipo)

    # ---------------------------- ACTUALIZAR ----------------------------
    def update(self, usuario_id, **kwargs):
        try:
            usuario = Usuario.objects.get(id=usuario_id)
            for key, value in kwargs.items():
                setattr(usuario, key, value)
            usuario.save()
            return usuario
        except ObjectDoesNotExist:
            return None

    # ---------------------------- ELIMINAR ----------------------------
    def delete(self, usuario_id):
        try:
            usuario = Usuario.objects.get(id=usuario_id)
            usuario.delete()
            return True
        except ObjectDoesNotExist:
            return False

    # ---------------------------- CONSULTAS EXTRA ----------------------------
    def search_by_nombre(self, texto):
        """Búsqueda parcial por nombre o apellido."""
        return Usuario.objects.filter(
            models.Q(nombre__icontains=texto) |
            models.Q(apellido__icontains=texto)
        )

    def get_activos(self):
        """Obtiene usuarios activos."""
        return Usuario.objects.filter(activo=True)

    def get_inactivos(self):
        """Obtiene usuarios inactivos."""
        return Usuario.objects.filter(activo=False)

    def desactivar(self, usuario_id):
        """Método administrativo: desactiva un usuario sin eliminarlo."""
        try:
            usuario = Usuario.objects.get(id=usuario_id)
            usuario.activo = False
            usuario.save()
            return usuario
        except ObjectDoesNotExist:
            return None

    def activar(self, usuario_id):
        """Activa un usuario previamente desactivado."""
        try:
            usuario = Usuario.objects.get(id=usuario_id)
            usuario.activo = True
            usuario.save()
            return usuario
        except ObjectDoesNotExist:
            return None

    # AUTENTICACIÓN BÁSICA (si no usas Django Auth)
    def verificar_credenciales(self, email, password_hash):
        """
        Valida login básico basado en email + hash.
        Retorna el usuario o None.
        """
        try:
            usuario = Usuario.objects.get(email=email)
            if usuario.password_hash == password_hash:
                return usuario
            return None
        except ObjectDoesNotExist:
            return None
