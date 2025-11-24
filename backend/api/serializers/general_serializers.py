from rest_framework import serializers
from api.models.usuario import Usuario
from api.models.prestador import PrestadorServicio
from api.models.servicio import ServicioTuristico
from api.models.denuncia import Denuncia
from api.models.calificacion import Calificacion
from api.models.turista import Turista

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class PrestadorServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrestadorServicio
        fields = '__all__'

class ServicioTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioTuristico
        fields = '__all__'

class DenunciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Denuncia
        fields = '__all__'

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = '__all__'

class TuristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turista
        fields = '__all__'
