from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permiso: Solo el dueño del objeto puede editarlo.
    Lectura permitida para autenticados.
    """

    def has_object_permission(self, request, view, obj):

        # Métodos seguros (GET, HEAD, OPTIONS) permitidos
        if request.method in permissions.SAFE_METHODS:
            return True

        # Prevenir errores si el user no está autenticado
        if not request.user or not request.user.is_authenticated:
            return False

        # Nota: "obj" debe ser un Usuario, o tener un atributo user/usuario
        # Ej: obj.usuario.id == request.user.id, según el modelo
        # Si el objeto es un Usuario:
        if hasattr(obj, "id"):
            return obj.id == request.user.id
        
        # Si el objeto tiene usuario relacionado (ej: PerfilTurista, Empresa, etc.)
        if hasattr(obj, "usuario"):
            return obj.usuario.id == request.user.id

        return False



class IsTurista(permissions.BasePermission):
    """
    Permite acceso solo a usuarios tipo TURISTA.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.nombre_tipo == "TURISTA"
        )

class IsEmpresa(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.nombre_tipo == "EMPRESA"
        )

class IsPrestador(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.nombre_tipo == "PRESTADOR"
        )
