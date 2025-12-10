from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True

        
        
        
        if hasattr(obj, 'empresa_prestadora') and obj.empresa_prestadora:
             if obj.empresa_prestadora.usuario == request.user:
                 return True
        if hasattr(obj, 'prestador_individual') and obj.prestador_individual:
             if obj.prestador_individual.usuario == request.user:
                 return True
                 
        
        if hasattr(obj, 'id_usuario'):
            return obj.id_usuario == request.user
            
        return False
