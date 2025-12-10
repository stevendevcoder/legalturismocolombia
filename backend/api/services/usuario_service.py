# services/usuario_service.py
from django.db import IntegrityError
from django.forms import ValidationError
from api.repository.usuario_repository import UsuarioRepo
from api.models.turista import Turista
from api.models.empresas_prestadoras import EmpresaPrestadora
from api.models.prestador_individual import PrestadorIndividual
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

Usuario = get_user_model()


class UsuarioService:

    # =======================================================
    # CREACIÓN DE USUARIO (El que arreglamos)
    # =======================================================
    @staticmethod
    def crear_usuario(data):
        """
        Crea un usuario y su perfil asociado (Turista, Empresa, etc.)
        """
        # 1. Extraer contraseña y tipo
        password = data.pop("password")
        tipo = data.get("nombre_tipo")
        
        # 2. Extraer datos de los perfiles para que no estorben al crear el Usuario base
        turista_data = data.pop("turista", None)
        empresa_data = data.pop("empresa", None)
        prestador_data = data.pop("prestador", None)

        # 3. Formatear fecha si viene como objeto datetime
        fecha = data.get("fecha_nacimiento")
        if hasattr(fecha, "date"):
            data["fecha_nacimiento"] = fecha.date()

        try:
            # 4. Crear el Usuario Base (Aquí 'data' ya está limpia de campos extra)
            usuario = UsuarioRepo.create_user(password=password, **data)
            
            # 5. Crear el Perfil Específico según el tipo
            if tipo == "TURISTA" and turista_data:
                Turista.objects.create(usuario=usuario, **turista_data)
                
            elif tipo == "EMPRESA" and empresa_data:
                EmpresaPrestadora.objects.create(usuario=usuario, **empresa_data)
                
            elif tipo == "PRESTADOR" and prestador_data:
                PrestadorIndividual.objects.create(usuario=usuario, **prestador_data)

            return usuario

        except IntegrityError as e:
            if "email" in str(e):
                raise ValidationError({"email": "Este email ya está registrado"})
            if "num_identificacion" in str(e):
                raise ValidationError({"num_identificacion": "Este número de identificación ya está registrado"})
            raise ValidationError({"error": "Error de integridad en la base de datos"})

    # =======================================================
    # GENERACIÓN DE TOKENS 
    # =======================================================
    
    @staticmethod
    def generar_tokens(usuario):
        """
        Genera tokens JWT (access y refresh) para el usuario.
        """
        refresh = RefreshToken.for_user(usuario)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }

    # =======================================================
    # OTROS MÉTODOS 
    # =======================================================
    @staticmethod
    def obtener_usuario_por_id(user_id):
        return UsuarioRepo.get_by_id(user_id)

    @staticmethod
    def actualizar_usuario(usuario, data):
        """
        Actualiza datos del usuario base Y de su perfil específico (Turista/Empresa).
        """
        # 1. Evitar que cambien datos sensibles o inmutables
        data.pop("nombre_tipo", None) 
        data.pop("email", None) # Generalmente el email no se cambia tan fácil
        data.pop("password", None) # La contraseña tiene su propio endpoint

        # 2. Extraer datos de perfiles
        turista_data = data.pop("turista", None)
        empresa_data = data.pop("empresa", None)
        prestador_data = data.pop("prestador", None)

        # 3. Actualizar Usuario Base
        if data:
            usuario = UsuarioRepo.update(usuario, data)

        # 4. Actualizar Perfil Específico
        if usuario.nombre_tipo == "TURISTA" and turista_data:
            Turista.objects.filter(usuario=usuario).update(**turista_data)

        elif usuario.nombre_tipo == "EMPRESA" and empresa_data:
            EmpresaPrestadora.objects.filter(usuario=usuario).update(**empresa_data)

        elif usuario.nombre_tipo == "PRESTADOR" and prestador_data:
            PrestadorIndividual.objects.filter(usuario=usuario).update(**prestador_data)

        return usuario

    @staticmethod
    def obtener_detalles_completos(usuario):
        
        from api.serializers.register_serializer import TuristaSerializer, EmpresaPrestadoraSerializer, PrestadorSerializer
        
        response = {
            "id": usuario.id,
            "email": usuario.email,
            "nombre": usuario.nombre,
            "apellido": usuario.apellido, 
            "nombre_tipo": usuario.nombre_tipo
        }

        if usuario.nombre_tipo == "TURISTA":
            turista = Turista.objects.filter(usuario=usuario).first()
            if turista:
                response["turista"] = TuristaSerializer(turista).data

        elif usuario.nombre_tipo == "EMPRESA":
            empresa = EmpresaPrestadora.objects.filter(usuario=usuario).first()
            if empresa:
                response["empresa"] = EmpresaPrestadoraSerializer(empresa).data
        
        elif usuario.nombre_tipo == "PRESTADOR":
            prestador = PrestadorIndividual.objects.filter(usuario=usuario).first()
            if prestador:
                response["prestador"] = PrestadorSerializer(prestador).data

        return response
