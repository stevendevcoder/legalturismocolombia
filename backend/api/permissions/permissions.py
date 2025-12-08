from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permiso personalizado para que solo el dueño del objeto pueda editarlo.
    """
    def has_object_permission(self, request, view, obj):
        # Métodos de lectura (GET, HEAD, OPTIONS) permitidos a cualquiera autenticado
        if request.method in permissions.SAFE_METHODS:
            return True

        # La escritura solo permitida si el objeto (Usuario) es el mismo que hace la request
        # Nota: Esto asume que tu autenticación llena request.user o request.auth['user_id']
        return obj.id == request.user.id

class IsTurista(permissions.BasePermission):
    """
    Permite acceso solo a usuarios tipo TURISTA.
    """
    def has_permission(self, request, view):
        return request.user and request.user.nombre_tipo == "TURISTA"