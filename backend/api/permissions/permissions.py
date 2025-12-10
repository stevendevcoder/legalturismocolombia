from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permiso: Solo el dueño del objeto puede editarlo.
    Lectura permitida para autenticados.
    """

    def has_object_permission(self, request, view, obj):

        
        if request.method in permissions.SAFE_METHODS:
            return True

        
        if not request.user or not request.user.is_authenticated:
            return False

        
        if hasattr(obj, "id"):
            return obj.id == request.user.id
        
        
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
