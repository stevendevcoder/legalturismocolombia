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
        
        categoria = request.query_params.get('categoria', None)
        ciudad = request.query_params.get('ciudad', None)

        empresas = EmpresaPrestadora.objects.all()
        individuales = PrestadorIndividual.objects.all()

        if categoria:
            empresas = empresas.filter(categoria_empresa=categoria)
            
            
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
        
        provider = None
        
        empresa = EmpresaPrestadora.objects.filter(pk=pk).first()
        if empresa:
            certs = empresa.certificados.all()
            return Response(CertificadoHabilidadSerializer(certs, many=True).data)
            
        individual = PrestadorIndividual.objects.filter(pk=pk).first()
        if individual:
            certs = individual.certificados.all()
            return Response(CertificadoHabilidadSerializer(certs, many=True).data)

        return Response(status=404)
