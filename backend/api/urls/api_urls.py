from django.urls import path
from api.views.auth_controller import (
    LoginAPIView, RegisterAPIView, LogoutAPIView
)
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
    MisDenunciasView,
    ListarCalificacionView,
    CrearCalificacionView
)

from api.views.provider_views import ProviderViewSet
from api.views.service_views import ServiceViewSet
from api.views.employee_views import EmpleadoViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views.usuario_controller import MeAPIView

router = DefaultRouter()
router.register(r'turistas', TuristaViewSet)
router.register(r'providers', ProviderViewSet, basename='provider')
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'employees', EmpleadoViewSet, basename='employee')

urlpatterns = [
    # --- Autenticación ---
    path('auth/register/', RegisterAPIView.as_view(), name='auth_register'),
    path('auth/logout/', LogoutAPIView.as_view(), name='auth_logout'),
    path('auth/me/', MeAPIView.as_view(), name='auth_me'),
    path('auth/login/', LoginAPIView.as_view(), name='auth_login'),
    path('users/profile/', MeAPIView.as_view(), name='user_profile'),
    # --- JWT Tokens ---
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('prestadores/registro/', RegistroPrestadorView.as_view(), name='registro_prestador'),
    path('servicios/buscar/', BusquedaServiciosView.as_view(), name='buscar_servicios'),
    path('qr/verificar/<str:codigo>/', VerificacionQRView.as_view(), name='verificar_qr'),
    path("prestadores/<int:prestador_id>/qr/", GenerarQRPrestadorView.as_view()),
    # Reseñas
    path('services/<int:id>/reviews/', ListarCalificacionView.as_view()),
    path('services/<int:id>/reviews/create/', CrearCalificacionView.as_view()),

    # Denuncias
    # Denuncias
    path('reports/', CrearDenunciaView.as_view()),
    path('reports/my-reports/', MisDenunciasView.as_view()),
] + router.urls
    
