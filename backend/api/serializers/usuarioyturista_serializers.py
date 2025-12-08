from rest_framework import serializers
from ..models.usuario import Usuario
from ..models.turista import Turista

# --- Serializer Base de Usuario ---
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        # Excluimos password_hash de la respuesta por seguridad
        exclude = ['password_hash']

# --- Serializer de Turista ---
class TuristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turista
        exclude = ['id_usuario'] # Se asocia internamente

# --- Serializer de Registro (Input) ---
class RegisterSerializer(serializers.Serializer):
    # Campos comunes
    nombre = serializers.CharField(max_length=100)
    apellido = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)
    fecha_nacimiento = serializers.DateTimeField()
    numero_telefonico = serializers.CharField(max_length=20)
    tipo_identificacion = serializers.CharField(max_length=50)
    num_identificacion = serializers.CharField(max_length=50)
    url_foto_documento = serializers.CharField(max_length=255)
    nombre_tipo = serializers.ChoiceField(choices=Usuario.TipoUsuario.choices)
    
    # Campos específicos de Turista (opcionales si no es turista, pero los validaremos)
    pais_residencia = serializers.CharField(max_length=100, required=False)
    idioma_preferido = serializers.CharField(max_length=100, required=False)
    contacto_emergencia_nombre = serializers.CharField(max_length=150, required=False)
    contacto_emergencia_telefono = serializers.CharField(max_length=20, required=False)

    def validate(self, data):
        # Validación: Si es Turista, los campos de turista son obligatorios
        if data.get('nombre_tipo') == Usuario.TipoUsuario.TURISTA:
            if not data.get('pais_residencia'):
                raise serializers.ValidationError({"pais_residencia": "Requerido para turistas."})
            # ... agregar validaciones para los otros campos de turista
        return data

# --- Serializer de Login ---
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)