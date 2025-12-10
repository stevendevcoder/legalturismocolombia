from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from api.services.filtro_servicios import filtrar_servicios
from api.services.qr_service import obtener_datos_prestador_por_qr
from api.services.turista_service import TuristaService
# from api.utils.interaccion import verificar_interaccion_real  <-- Removed broken import

from api.serializers.user_serializers import TuristaSerializer
from api.models.turista import Turista

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

class TuristaViewSet(viewsets.ModelViewSet):
    queryset = Turista.objects.all()
    serializer_class = TuristaSerializer

