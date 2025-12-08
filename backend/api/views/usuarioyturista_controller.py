from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from ..services import AuthService
from ..serializers import RegisterSerializer, LoginSerializer, UsuarioSerializer, TuristaSerializer
from ..repository.usuario_repository import UsuarioRepository
from ..permissions import IsOwnerOrReadOnly

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            auth_service = AuthService()
            try:
                usuario = auth_service.registrar_usuario(serializer.validated_data)
                return Response({
                    "message": "Usuario creado exitosamente",
                    "user_id": usuario.id
                }, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            auth_service = AuthService()
            try:
                data = auth_service.login(
                    email=serializer.validated_data['email'],
                    password=serializer.validated_data['password']
                )
                # Serializamos el usuario para devolverlo en el login
                user_data = UsuarioSerializer(data['usuario']).data
                return Response({
                    'tokens': {
                        'refresh': data['refresh'],
                        'access': data['access']
                    },
                    'user': user_data
                }, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Gracias a SimpleJWT, request.user debería estar poblado. 
        # Si tu modelo Usuario no es el standard de Django, SimpleJWT retornará 
        # un objeto token, por lo que usaremos el ID del token para buscar en el repo.
        
        repo = UsuarioRepository()
        # Asumiendo que configuraste el AUTH_USER_MODEL o SimpleJWT correctamente:
        user = request.user 
        
        serializer = UsuarioSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Blacklist del refresh token
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout exitoso"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Token inválido"}, status=status.HTTP_400_BAD_REQUEST)