from rest_framework import serializers
from api.models.empresas_prestadoras import EmpresaPrestadora
from api.models.prestador_individual import PrestadorIndividual
from api.models.certificados import CertificadoHabilidad
from api.serializers.user_serializers import UsuarioSerializer

class CertificadoHabilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificadoHabilidad
        fields = '__all__'

class EmpresaPrestadoraSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(source='id_usuario', read_only=True)
    certificados = CertificadoHabilidadSerializer(many=True, read_only=True)
    
    class Meta:
        model = EmpresaPrestadora
        fields = '__all__'

class PrestadorIndividualSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(source='id_usuario', read_only=True)
    certificados = CertificadoHabilidadSerializer(many=True, read_only=True)

    class Meta:
        model = PrestadorIndividual
        fields = '__all__'

# Serializer that can represent either provider type in a list?
# For /api/providers/ endpoint, we might want a polymorphic representation or just combine them in the view.
