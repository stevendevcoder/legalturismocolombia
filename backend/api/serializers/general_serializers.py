from rest_framework import serializers
from api.models import Usuario, EmpresaPrestadora, PrestadorIndividual, ServicioTuristico, Denuncia, Calificacion, Turista

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

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class TuristaSerializer(serializers.ModelSerializer):
    id_usuarios_fk = UsuarioSerializer()

    class Meta:
        model = Turista
        fields = '__all__'

    def create(self, validated_data):
        usuario_data = validated_data.pop('id_usuarios_fk')
        usuario = Usuario.objects.create(**usuario_data)
        turista = Turista.objects.create(id_usuarios_fk=usuario, **validated_data)
        return turista

    def update(self, instance, validated_data):
        usuario_data = validated_data.pop('id_usuarios_fk', {})
        usuario = instance.id_usuarios_fk
        for attr, value in usuario_data.items():
            setattr(usuario, attr, value)
        usuario.save()
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
