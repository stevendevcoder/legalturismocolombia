from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from api.services.filtro_servicios import filtrar_servicios
from api.services.qr_service import obtener_datos_prestador_por_qr
from api.utils.interaccion import verificar_interaccion_real
from api.serializers.general_serializers import TuristaSerializer
from api.services.qr_service import generar_qr_para_prestador
from api.models.turista import Turista
from api.models.denuncia import Denuncia
from api.serializers.general_serializers import DenunciaSerializer
from api.serializers.general_serializers import CalificacionSerializer
from api.models.calificacion import Calificacion
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class RegistroPrestadorView(APIView):
    def post(self, request):
        return Response({"mensaje": "Registro exitoso"}, status=status.HTTP_201_CREATED)

@method_decorator(csrf_exempt, name='dispatch')
class CrearDenunciaView(APIView):
    def post(self, request):
        return Response({"mensaje": "Denuncia creada"}, status=status.HTTP_201_CREATED)
    serializer_class = DenunciaSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class MisDenunciasView(generics.ListAPIView):
    serializer_class = DenunciaSerializer
    permission_classes = [permissions.AllowAny]  # SOLO PARA PRUEBAS

    def get_queryset(self):
        return Denuncia.objects.all()

class BusquedaServiciosView(APIView):
    def get(self, request):
        return Response({"resultados": []}, status=status.HTTP_200_OK)

class VerificacionQRView(APIView):
    def get(self, request, codigo):
        return Response({"datos": "info del prestador"}, status=status.HTTP_200_OK)

class TuristaViewSet(viewsets.ModelViewSet):
    queryset = Turista.objects.all()
    serializer_class = TuristaSerializer
    
class ListarCalificacionView(generics.ListAPIView):
    serializer_class = CalificacionSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        servicio_id = self.kwargs['id']
        return Calificacion.objects.filter(prestador_id=servicio_id)

class CrearCalificacionView(generics.CreateAPIView):
    serializer_class = CalificacionSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        prestador_id = self.kwargs["id"]
        serializer.save(
            usuario=self.request.user,
            prestador_id=prestador_id
        )

class GenerarQRPrestadorView(APIView):
    def get(self, request, prestador_id):
        url = f"http://127.0.0.1:8000/api/prestadores/{prestador_id}/"

        nombre_archivo = f"prestador_{prestador_id}.png"
        qr_url = generar_qr_para_prestador(url, nombre_archivo)

        return Response({
            "mensaje": "QR generado correctamente",
            "qr_url": qr_url
        })