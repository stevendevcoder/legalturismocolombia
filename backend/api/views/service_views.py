from rest_framework import viewsets, permissions
from api.models.servicio import CardServicioVenta
from api.models.empresas_prestadoras import EmpresaPrestadora
from api.models.prestador_individual import PrestadorIndividual
from api.serializers.service_serializers import ServiceSerializer
from api.permissions.general_permissions import IsOwnerOrReadOnly

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = CardServicioVenta.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = CardServicioVenta.objects.all()
        
        # Filters
        precio = self.request.query_params.get('precio', None)
        tipo = self.request.query_params.get('tipo', None)
        calificacion = self.request.query_params.get('calificacion', None)
        
        if precio:
             queryset = queryset.filter(unidad_precio=precio) # Note: Exact match on CharField
        if tipo:
             queryset = queryset.filter(categoria_servicio=tipo)
             
        # Calificacion Logic would need aggregation annotation
        
        return queryset

    def perform_create(self, serializer):
        # Assign provider based on logged in user
        user = self.request.user
        empresa = EmpresaPrestadora.objects.filter(id_usuario=user).first()
        individual = PrestadorIndividual.objects.filter(id_usuario=user).first()
        
        if empresa:
            serializer.save(empresa_prestadora=empresa)
        elif individual:
            serializer.save(prestador_individual=individual)
        else:
            # Handle case where user is not a provider (maybe error?)
            serializer.save() 
