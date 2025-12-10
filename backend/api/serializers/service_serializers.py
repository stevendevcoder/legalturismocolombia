from rest_framework import serializers
from api.models.servicio import CardServicioVenta
from api.serializers.provider_serializers import EmpresaPrestadoraSerializer, PrestadorIndividualSerializer

class ServiceSerializer(serializers.ModelSerializer):
    
    empresa_prestadora_detail = EmpresaPrestadoraSerializer(source='empresa_prestadora', read_only=True)
    prestador_individual_detail = PrestadorIndividualSerializer(source='prestador_individual', read_only=True)

    
    url_imagen_principal = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = CardServicioVenta
        fields = '__all__'
