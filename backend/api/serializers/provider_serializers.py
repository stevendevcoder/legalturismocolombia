from rest_framework import serializers
from api.models.empresas_prestadoras import EmpresaPrestadora
from api.models.prestador_individual import PrestadorIndividual
from api.models.certificados import Certificado
from api.serializers.user_serializers import UsuarioSerializer

class CertificadoHabilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificado
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


