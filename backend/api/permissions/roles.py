from rest_framework.permissions import BasePermission

class EsPrestador(BasePermission):
    """
    Permiso personalizado para verificar si el usuario tiene rol de Prestador.
    """
    def has_permission(self, request, view):
        # Lógica para verificar rol
        return request.user.is_authenticated and request.user.roles.filter(nombre='Prestador').exists()

class EsAdministrador(BasePermission):
    """
    Permiso para administradores.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff
