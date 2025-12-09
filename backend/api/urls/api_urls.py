from django.urls import path
from django.contrib import admin
from api.views.auth_controller import (
    LoginAPIView, RegisterAPIView, LogoutAPIView
)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views.usuario_controller import MeAPIView, UserProfileUpdateView

urlpatterns = [
    # --- Autenticación ---
    path('auth/register/', RegisterAPIView.as_view(), name='auth_register'),
    path('auth/logout/', LogoutAPIView.as_view(), name='auth_logout'),
    path('auth/me/', MeAPIView.as_view(), name='auth_me'),
    path('auth/login/', LoginAPIView.as_view(), name='auth_login'),
    path('users/profile/', UserProfileUpdateView.as_view(), name='update_profile'),
    # --- JWT Tokens ---
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]