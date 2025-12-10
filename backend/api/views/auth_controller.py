from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from api.serializers.register_serializer import (
    RegistrationSerializer, UsuarioSerializer
)
from api.services.usuario_service import UsuarioService

class RegisterAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            usuario = UsuarioService.crear_usuario(serializer.validated_data)

            # generar tokens del usuario recién creado
            tokens = UsuarioService.generar_tokens(usuario)

            return Response({
                "message": "Usuario creado correctamente",
                "usuario": UsuarioSerializer(usuario).data,
                "tokens": tokens
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        # Autenticación manual porque usas email como USERNAME_FIELD
        usuario = authenticate(request, email=email, password=password)

        if usuario is None:
            return Response(
                {"error": "Credenciales inválidas"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        tokens = UsuarioService.generar_tokens(usuario)

        return Response({
            "message": "Inicio de sesión exitoso",
            "usuario": UsuarioSerializer(usuario).data,
            "role": usuario.nombre_tipo,
            "user_id": usuario.id,
            "tokens": tokens
        })


class LogoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if refresh_token is None:
                return Response({"error": "Se requiere el refresh token"}, 
                                status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message": "Sesión cerrada correctamente"},
                            status=status.HTTP_205_RESET_CONTENT)

        except Exception:
            return Response({"error": "Token inválido o expirado"},
                            status=status.HTTP_400_BAD_REQUEST)
