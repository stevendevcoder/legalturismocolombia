from rest_framework import serializers
from api.models.servicio import CardServicioVenta
from api.serializers.provider_serializers import EmpresaPrestadoraSerializer, PrestadorIndividualSerializer

class ServiceSerializer(serializers.ModelSerializer):
    # Optional: Display provider info
    empresa_prestadora_detail = EmpresaPrestadoraSerializer(source='empresa_prestadora', read_only=True)
    prestador_individual_detail = PrestadorIndividualSerializer(source='prestador_individual', read_only=True)

    # Relax validation for this field to allow handling it in the view
    url_imagen_principal = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = CardServicioVenta
        fields = '__all__'
