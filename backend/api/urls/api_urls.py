from django.urls import path
from api.views.general_views import (
    RegistroPrestadorView, 
    CrearDenunciaView, 
    BusquedaServiciosView, 
    VerificacionQRView
)

urlpatterns = [
    path('prestadores/registro/', RegistroPrestadorView.as_view(), name='registro_prestador'),
    path('denuncias/crear/', CrearDenunciaView.as_view(), name='crear_denuncia'),
    path('servicios/buscar/', BusquedaServiciosView.as_view(), name='buscar_servicios'),
    path('qr/verificar/<str:codigo>/', VerificacionQRView.as_view(), name='verificar_qr'),
]
