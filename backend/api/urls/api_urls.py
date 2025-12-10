from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.general_views import CrearDenunciaView, MisDenunciasView
from api.views.general_views import GenerarQRPrestadorView
from api.views.general_views import (
    RegistroPrestadorView,
    CrearDenunciaView,
    BusquedaServiciosView,
    VerificacionQRView,
    TuristaViewSet,
    CrearDenunciaView,
    MisDenunciasView,
    ListarCalificacionView,
    CrearCalificacionView
)

router = DefaultRouter()
router.register(r'turistas', TuristaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('prestadores/registro/', RegistroPrestadorView.as_view(), name='registro_prestador'),
    path('servicios/buscar/', BusquedaServiciosView.as_view(), name='buscar_servicios'),
    path('qr/verificar/<str:codigo>/', VerificacionQRView.as_view(), name='verificar_qr'),
    path("prestadores/<int:prestador_id>/qr/", GenerarQRPrestadorView.as_view()),
    # Reseñas
    path('services/<int:id>/reviews/', ListarCalificacionView.as_view()),
    path('services/<int:id>/reviews/create/', CrearCalificacionView.as_view()),

    # Denuncias
    path('reports/', CrearDenunciaView.as_view()),
    path('reports/my-reports/', MisDenunciasView.as_view()),
    
    
    
]
