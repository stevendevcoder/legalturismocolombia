from rest_framework.permissions import BasePermission

class EsPrestador(BasePermission):
    def has_permission(self, request, view):
        # Lógica para verificar rol
        return request.user.is_authenticated and request.user.roles.filter(nombre='Prestador').exists()

class EsAdministrador(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff
