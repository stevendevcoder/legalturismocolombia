from rest_framework import serializers
from django.conf import settings
from api.models.usuario import Usuario
from api.models.turista import Turista
from api.models.empresas_prestadoras import EmpresaPrestadora
from api.models.prestador_individual import PrestadorIndividual  # si existe

class TuristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turista
        fields = ['pais_residencia','idioma_preferido','contacto_emergencia_nombre','contacto_emergencia_telefono']

class EmpresaPrestadoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresaPrestadora
        fields = ['nit_empresa','nombre_razon_social','direccion','categoria_empresa','rnt_empresa','url_rnt_certificado','matricula_mercantil','url_cert_camara_comercio']

class PrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrestadorIndividual
        fields = ['profesion_servicio_principal','estado_afiliacion_seguridad','url_rut','matricula_comerciante_ind','municipio_operacion','lugar_prestacion_servicio','url_permiso_alcaldia']

class UsuarioSerializer(serializers.ModelSerializer):
    fecha_nacimiento = serializers.SerializerMethodField()

    class Meta:
        model = Usuario
        fields = ['id','email','nombre','apellido','fecha_nacimiento',
                  'numero_telefonico','tipo_identificacion','num_identificacion',
                  'url_foto_documento','nombre_tipo','activo']

    def get_fecha_nacimiento(self, obj):
        fecha = obj.fecha_nacimiento
        return fecha.date() if hasattr(fecha, 'date') else fecha

class RegistrationSerializer(serializers.Serializer):
    # Datos básicos del usuario
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=6)
    nombre = serializers.CharField()
    apellido = serializers.CharField()
    fecha_nacimiento = serializers.DateField()
    numero_telefonico = serializers.CharField()
    tipo_identificacion = serializers.CharField()
    num_identificacion = serializers.CharField()
    url_foto_documento = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    # Tipo de usuario
    nombre_tipo = serializers.ChoiceField(choices=Usuario.TipoUsuario.choices)

    # Submodelos
    turista = TuristaSerializer(required=False)
    empresa = EmpresaPrestadoraSerializer(required=False)
    prestador = PrestadorSerializer(required=False)

    def to_internal_value(self, data):
        # Convertir QueryDict a diccionario plano python mutable
        if hasattr(data, 'dict'):
            data = data.dict()
        else:
            data = data.copy() # Si ya es dict, copiamos

        tipo = data.get("nombre_tipo")

        # Helper para mover campos planos a un diccionario anidado
        def nest_data(serializer_cls, target_key):
            fields = serializer_cls().fields.keys()
            nested_dict = {}
            for field in fields:
                if field in data:
                    nested_dict[field] = data.get(field)
            
            if nested_dict:
                data[target_key] = nested_dict

        if tipo == Usuario.TipoUsuario.TURISTA:
            nest_data(TuristaSerializer, "turista")

        elif tipo == Usuario.TipoUsuario.EMPRESA:
            nest_data(EmpresaPrestadoraSerializer, "empresa")

        elif tipo == Usuario.TipoUsuario.PRESTADOR:
            nest_data(PrestadorSerializer, "prestador")

        return super().to_internal_value(data)

    def validate(self, data):
        tipo = data.get("nombre_tipo")

        # Validaciones por subtipo
        if tipo == Usuario.TipoUsuario.TURISTA and "turista" not in data:
            raise serializers.ValidationError({"turista": "Debes enviar los datos de turista."})

        if tipo == Usuario.TipoUsuario.EMPRESA and "empresa" not in data:
            raise serializers.ValidationError({"empresa": "Debes enviar los datos de empresa."})

        if tipo == Usuario.TipoUsuario.PRESTADOR and "prestador" not in data:
            raise serializers.ValidationError({"prestador": "Debes enviar los datos de prestador individual."})

        return data

    def to_representation(self, instance):
        data = UsuarioSerializer(instance).data

        # Agregar datos del subtipo
        if instance.nombre_tipo == Usuario.TipoUsuario.TURISTA and hasattr(instance, "perfil_turista"):
            data["turista"] = TuristaSerializer(instance.perfil_turista).data

        if instance.nombre_tipo == Usuario.TipoUsuario.EMPRESA:
            empresa = instance.empresa_prestadora.first()
            if empresa:
                data["empresa"] = EmpresaPrestadoraSerializer(empresa).data

        if instance.nombre_tipo == Usuario.TipoUsuario.PRESTADOR:
            prestador = instance.prestador_individual.first()
            if prestador:
                data["prestador"] = PrestadorSerializer(prestador).data

        return data
