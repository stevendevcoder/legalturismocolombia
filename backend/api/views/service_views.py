from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
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
        queryset = CardServicioVenta.objects.filter(is_active=True)
        
        # Filters
        mine = self.request.query_params.get('mine', None)
        precio = self.request.query_params.get('precio', None)
        tipo = self.request.query_params.get('tipo', None)
        calificacion = self.request.query_params.get('calificacion', None)

        if mine == 'true' and self.request.user.is_authenticated:
            # Filter by current user (check both provider types)
            user = self.request.user
            empresa = EmpresaPrestadora.objects.filter(usuario=user).first()
            individual = PrestadorIndividual.objects.filter(usuario=user).first()
            
            if empresa:
                queryset = queryset.filter(empresa_prestadora=empresa)
            elif individual:
                queryset = queryset.filter(prestador_individual=individual)
            else:
                queryset = queryset.none() # Authenticated but not a provider
        
        if precio:
             queryset = queryset.filter(unidad_precio=precio) # Note: Exact match on CharField
        if tipo:
             queryset = queryset.filter(categoria_servicio=tipo)
             
        # Calificacion Logic would need aggregation annotation
        
        return queryset

    def perform_create(self, serializer):
        # Assign provider based on logged in user
        user = self.request.user
        empresa = EmpresaPrestadora.objects.filter(usuario=user).first()
        individual = PrestadorIndividual.objects.filter(usuario=user).first()
        
        # Handle valid image upload manually since we aren't using ImageField yet
        extras = {}
        if 'imagen' in self.request.FILES:
            image_file = self.request.FILES['imagen']
            file_name = default_storage.save(f"services/{image_file.name}", ContentFile(image_file.read()))
            # Assuming MEDIA_URL is /media/ 
            extras['url_imagen_principal'] = f"/media/{file_name}"
        elif not serializer.validated_data.get('url_imagen_principal'):
             # Default placeholder if nothing provided
             extras['url_imagen_principal'] = "https://via.placeholder.com/300x200?text=Sin+Imagen"
        
        if empresa:
            serializer.save(empresa_prestadora=empresa, **extras)
        elif individual:
            serializer.save(prestador_individual=individual, **extras)
        else:
            # Handle case where user is not a provider (maybe error?)
            serializer.save(**extras) 

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=204) 
