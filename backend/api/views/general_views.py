from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from api.services.filtro_servicios import filtrar_servicios
from api.services.qr_service import obtener_datos_prestador_por_qr
from api.services.turista_service import TuristaService
from api.utils.interaccion import verificar_interaccion_real
from api.serializers.general_serializers import TuristaSerializer

class RegistroPrestadorView(APIView):
    def post(self, request):
        return Response({"mensaje": "Registro exitoso"}, status=status.HTTP_201_CREATED)

class CrearDenunciaView(APIView):
    def post(self, request):
        return Response({"mensaje": "Denuncia creada"}, status=status.HTTP_201_CREATED)

class BusquedaServiciosView(APIView):
    def get(self, request):
        return Response({"resultados": []}, status=status.HTTP_200_OK)

class VerificacionQRView(APIView):
    def get(self, request, codigo):
        return Response({"datos": "info del prestador"}, status=status.HTTP_200_OK)

class TuristaViewSet(viewsets.ViewSet):
    def list(self, request):
        turistas = TuristaService.listar_turistas()
        serializer = TuristaSerializer(turistas, many=True)
        return Response(serializer.data)

    def search(self, request, pk=None):
        turista = TuristaService.obtener_turista(pk)
        if not turista:
            return Response({"error": "Turista no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TuristaSerializer(turista)
        return Response(serializer.data)

    def create(self, request):
        serializer = TuristaSerializer(data=request.data)
        if serializer.is_valid():
            turista = TuristaService.crear_turista(serializer.validated_data)
            serializer = TuristaSerializer(turista)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = TuristaSerializer(data=request.data)
        if serializer.is_valid():
            turista = TuristaService.actualizar_turista(pk, serializer.validated_data)
            if not turista:
                return Response({"error": "Turista no encontrado"}, status=status.HTTP_404_NOT_FOUND)
            serializer = TuristaSerializer(turista)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        if TuristaService.eliminar_turista(pk):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Turista no encontrado"}, status=status.HTTP_404_NOT_FOUND)
