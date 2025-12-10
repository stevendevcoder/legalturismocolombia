from rest_framework import serializers
from api.models.usuario import Usuario
from api.models.turista import Turista

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'numero_telefonico', 'tipo_identificacion', 'num_identificacion', 'url_foto_documento', 'nombre_tipo']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class TuristaSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(source='id_usuario')

    class Meta:
        model = Turista
        fields = ['id', 'usuario', 'pais_residencia', 'idioma_preferido', 'contacto_emergencia_nombre', 'contacto_emergencia_telefono']

    def create(self, validated_data):
        usuario_data = validated_data.pop('id_usuario')
        # Create user properly
        usuario_serializer = UsuarioSerializer(data=usuario_data)
        usuario_serializer.is_valid(raise_exception=True)
        usuario = usuario_serializer.save()
        
        turista = Turista.objects.create(id_usuario=usuario, **validated_data)
        return turista
    
    def update(self, instance, validated_data):
        usuario_data = validated_data.pop('id_usuario', None)
        if usuario_data:
            usuario = instance.id_usuario
            for attr, value in usuario_data.items():
                setattr(usuario, attr, value)
            usuario.save()
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
