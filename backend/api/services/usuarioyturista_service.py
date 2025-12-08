from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed, ValidationError

# Importa tus repositorios
from ..repository.usuario_repository import UsuarioRepository
from ..repository.turista_repository import TuristaRepository
from ..models.usuario import Usuario

class AuthService:
    def __init__(self):
        self.usuario_repo = UsuarioRepository()
        self.turista_repo = TuristaRepository()

    def registrar_usuario(self, data):
        """
        Maneja la lógica completa de registro:
        1. Validar unicidad.
        2. Hashear password.
        3. Crear Usuario Base.
        4. Si es Turista, crear perfil Turista.
        """
        # 1. Validar unicidad (Email y Documento)
        if self.usuario_repo.get_by_email(data['email']):
            raise ValidationError({"email": "El correo ya está registrado."})
        
        if self.usuario_repo.get_by_identificacion(data['num_identificacion']):
            raise ValidationError({"num_identificacion": "El documento ya existe."})

        # 2. Hashear password (Seguridad)
        hashed_pwd = make_password(data['password'])

        # 3. Crear Usuario Base usando el Repo
        nuevo_usuario = self.usuario_repo.create(
            nombre=data['nombre'],
            apellido=data['apellido'],
            fecha_nacimiento=data['fecha_nacimiento'],
            email=data['email'],
            password_hash=hashed_pwd, # Guardamos el hash, no el texto plano
            numero_telefonico=data['numero_telefonico'],
            tipo_identificacion=data['tipo_identificacion'],
            num_identificacion=data['num_identificacion'],
            url_foto_documento=data['url_foto_documento'],
            nombre_tipo=data['nombre_tipo']
        )

        # 4. Crear Perfil Específico (Factory pattern simplificado)
        if nuevo_usuario.nombre_tipo == Usuario.TipoUsuario.TURISTA:
            self.turista_repo.create(
                pais_residencia=data['pais_residencia'],
                idioma_preferido=data['idioma_preferido'],
                contacto_emergencia_nombre=data['contacto_emergencia_nombre'],
                contacto_emergencia_telefono=data['contacto_emergencia_telefono'],
                id_usuario=nuevo_usuario
            )
        
        return nuevo_usuario

    def login(self, email, password):
        """
        Verifica credenciales y genera Tokens JWT.
        """
        usuario = self.usuario_repo.get_by_email(email)

        # Verificar si existe y si la contraseña coincide (usando check_password de Django)
        if not usuario or not check_password(password, usuario.password_hash):
            raise AuthenticationFailed("Credenciales inválidas")

        if not usuario.activo:
            raise AuthenticationFailed("Usuario inactivo")

        # Generar Tokens JWT manualmente
        refresh = RefreshToken.for_user(usuario)
        
        # Agregamos claims personalizados al token si es necesario
        refresh['nombre_tipo'] = usuario.nombre_tipo
        refresh['email'] = usuario.email

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'usuario': usuario
        }