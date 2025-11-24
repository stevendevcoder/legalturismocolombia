from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.general_views import (
    RegistroPrestadorView,
    CrearDenunciaView,
    BusquedaServiciosView,
    VerificacionQRView,
    TuristaViewSet
)

router = DefaultRouter()
router.register(r'turistas', TuristaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('prestadores/registro/', RegistroPrestadorView.as_view(), name='registro_prestador'),
    path('denuncias/crear/', CrearDenunciaView.as_view(), name='crear_denuncia'),
    path('servicios/buscar/', BusquedaServiciosView.as_view(), name='buscar_servicios'),
    path('qr/verificar/<str:codigo>/', VerificacionQRView.as_view(), name='verificar_qr'),
]
