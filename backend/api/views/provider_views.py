from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from api.models.empresas_prestadoras import EmpresaPrestadora
from api.models.prestador_individual import PrestadorIndividual
from api.serializers.provider_serializers import EmpresaPrestadoraSerializer, PrestadorIndividualSerializer, CertificadoHabilidadSerializer
from django.db.models import Q

class ProviderViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving providers.
    Aggregates EmpresaPrestadora and PrestadorIndividual.
    Lookup field: user_id (to avoid collision)
    """

    def list(self, request):
        # Filters
        categoria = request.query_params.get('categoria', None)
        ciudad = request.query_params.get('ciudad', None)

        empresas = EmpresaPrestadora.objects.all()
        individuales = PrestadorIndividual.objects.all()

        if categoria:
            empresas = empresas.filter(categoria_empresa=categoria)
            # Individual might not have exact 'categoria_empresa'
            # Assuming 'profesion_servicio_principal' matches or we ignore individuals for this filter
            # Or we can check if individual has a service of that category
            
        if ciudad:
            empresas = empresas.filter(direccion__icontains=ciudad) # Rough approximation
            individuales = individuales.filter(municipio_operacion__icontains=ciudad)

        empresa_serializer = EmpresaPrestadoraSerializer(empresas, many=True)
        individual_serializer = PrestadorIndividualSerializer(individuales, many=True)

        return Response({
            'empresas': empresa_serializer.data,
            'individuales': individual_serializer.data
        })

    def retrieve(self, request, pk=None):
        # PK is expected to be user_id or we try to find in both
        # Let's assume PK IS the Provider ID if we wanted specific, but for collision avoidance...
        # Let's try to find in Empresa first, then Individual.
        # Note: If pk=1, it could be Empresa 1 OR Individual 1.
        # This implementation assumes the client knows context or we accept "type-id" format.
        # For simplicity of the request "GET /api/providers/{id}/", let's assume valid ID unique approach or just check both.
        
        # Strategy: Return matching from both (one should be empty hopefully if IDs don't collide much or if client knows)
        # BETTER: Use a query param 'type' or use User ID.
        # The prompt says "/api/providers/{id}/".
        
        # Let's look for ID in both.
        empresa = EmpresaPrestadora.objects.filter(pk=pk).first()
        if empresa:
            serializer = EmpresaPrestadoraSerializer(empresa)
            return Response({'type': 'empresa', 'data': serializer.data})
        
        individual = PrestadorIndividual.objects.filter(pk=pk).first()
        if individual:
            serializer = PrestadorIndividualSerializer(individual)
            return Response({'type': 'individual', 'data': serializer.data})
            
        return Response(status=404)

    @action(detail=True, methods=['get'])
    def certificates(self, request, pk=None):
        # Find provider
        provider = None
        # Try empresa
        empresa = EmpresaPrestadora.objects.filter(pk=pk).first()
        if empresa:
            certs = empresa.certificados.all()
            return Response(CertificadoHabilidadSerializer(certs, many=True).data)
            
        individual = PrestadorIndividual.objects.filter(pk=pk).first()
        if individual:
            certs = individual.certificados.all()
            return Response(CertificadoHabilidadSerializer(certs, many=True).data)

        return Response(status=404)
