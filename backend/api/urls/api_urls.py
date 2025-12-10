from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.general_views import (
    RegistroPrestadorView,
    CrearDenunciaView,
    BusquedaServiciosView,
    VerificacionQRView,
    TuristaViewSet
)

from api.views.provider_views import ProviderViewSet
from api.views.service_views import ServiceViewSet

router = DefaultRouter()
router.register(r'turistas', TuristaViewSet)
router.register(r'providers', ProviderViewSet, basename='provider')
router.register(r'services', ServiceViewSet, basename='service')

urlpatterns = [
    path('', include(router.urls)),
    path('prestadores/registro/', RegistroPrestadorView.as_view(), name='registro_prestador'),
    path('denuncias/crear/', CrearDenunciaView.as_view(), name='crear_denuncia'),
    path('servicios/buscar/', BusquedaServiciosView.as_view(), name='buscar_servicios'),
    path('qr/verificar/<str:codigo>/', VerificacionQRView.as_view(), name='verificar_qr'),
]
