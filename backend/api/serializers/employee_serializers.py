from rest_framework import serializers
from api.models.empleados_registrados import EmpleadoRegistrado
from api.serializers.user_serializers import UsuarioSerializer

class EmpleadoRegistradoSerializer(serializers.ModelSerializer):
    id_usuario_fk_detail = UsuarioSerializer(source='id_usuario_fk', read_only=True)
    
    class Meta:
        model = EmpleadoRegistrado
        fields = '__all__'
        read_only_fields = ['nit_empresa_fk']
