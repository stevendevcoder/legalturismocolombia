from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        # Check if obj has 'id_usuario' (Provider) or related owner field.
        
        # For Service (CardServicioVenta)
        if hasattr(obj, 'empresa_prestadora') and obj.empresa_prestadora:
             if obj.empresa_prestadora.id_usuario == request.user:
                 return True
        if hasattr(obj, 'prestador_individual') and obj.prestador_individual:
             if obj.prestador_individual.id_usuario == request.user:
                 return True
                 
        # For Provider Profiles
        if hasattr(obj, 'id_usuario'):
            return obj.id_usuario == request.user
            
        return False
