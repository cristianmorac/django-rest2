from django.urls import path
from users.api.views import RegisterView,UserView

# simple-jwt
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('auth/register',RegisterView.as_view()),
    # url Token y token refresh
    path('auth/login',TokenObtainPairView.as_view()),
    path('auth/token/refresh',TokenRefreshView.as_view()),
    # datos del usuario
    path('auth/me',UserView.as_view())
]