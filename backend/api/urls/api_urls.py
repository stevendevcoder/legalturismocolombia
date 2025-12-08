from django.urls import path
from api.views.usuarioyturista_controller import (
    LoginView, RegisterView, LogoutView, MeView
)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from legalturismocolombia.backend.api import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    # --- Autenticación ---
    path('auth/register/', RegisterView.as_view(), name='auth_register'),
    path('auth/login/', LoginView.as_view(), name='auth_login'),
    path('auth/logout/', LogoutView.as_view(), name='auth_logout'),
    path('auth/me/', MeView.as_view(), name='auth_me'),
    # --- JWT Tokens ---
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]