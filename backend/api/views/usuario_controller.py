from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from ..services.usuario_service import UsuarioService

# 1. Endpoint: GET /api/auth/me/
class MeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        usuario = UsuarioService.obtener_usuario_por_id(request.user.id)
        data = UsuarioService.obtener_detalles_completos(usuario)
        return Response(data)

    def patch(self, request):
        usuario = request.user
        try:
            # Llamamos al servicio para actualizar (incluyendo datos anidados de Turista/Empresa)
            usuario_actualizado = UsuarioService.actualizar_usuario(usuario, request.data)
            
            # Devolvemos los datos ya actualizados
            data = UsuarioService.obtener_detalles_completos(usuario_actualizado)
            return Response(data, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)