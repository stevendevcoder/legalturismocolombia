from rest_framework import viewsets, generics, views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.models import (
    Usuario,
    Turista, 
    EmpresaPrestadora, 
    PrestadorIndividual,
    Denuncia,
    CalificacionServicioUsuario,
)
from api.models.servicio import CardServicioVenta
from api.serializers.general_serializers import (
    TuristaSerializer,
    DenunciaSerializer,
    CalificacionSerializer,
    ServicioTuristicoSerializer
)


class TuristaViewSet(viewsets.ModelViewSet):
    queryset = Turista.objects.all()
    serializer_class = TuristaSerializer
    permission_classes = [IsAuthenticated]

class CrearDenunciaView(generics.CreateAPIView):
    queryset = Denuncia.objects.all()
    serializer_class = DenunciaSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class MisDenunciasView(generics.ListAPIView):
    serializer_class = DenunciaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Denuncia.objects.filter(usuario=self.request.user)

class RegistroPrestadorView(views.APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        
        return Response({"message": "Registro de prestador no implementado aun."}, status=status.HTTP_501_NOT_IMPLEMENTED)

class BusquedaServiciosView(generics.ListAPIView):
    serializer_class = ServicioTuristicoSerializer
    queryset = CardServicioVenta.objects.all()
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.query_params.get('q')
        if query:
            queryset = queryset.filter(titulo_card__icontains=query)
        return queryset

class GenerarQRPrestadorView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, prestador_id):
        return Response({"qr_code": "placeholder_qr_string"})

class VerificacionQRView(views.APIView):
    permission_classes = [AllowAny]

    def get(self, request, codigo):
        return Response({"verified": True, "codigo": codigo})

class ListarCalificacionView(generics.ListAPIView):
    serializer_class = CalificacionSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        service_id = self.kwargs.get('id')
        return CalificacionServicioUsuario.objects.filter(servicio_id=service_id)

class CrearCalificacionView(generics.CreateAPIView):
    serializer_class = CalificacionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        service_id = self.kwargs.get('id')
        serializer.save(usuario=self.request.user, servicio_id=service_id)
