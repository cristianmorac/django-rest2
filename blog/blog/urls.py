from django.contrib import admin
from django.urls import path, include


# drf_yasg
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# importar cuando es modelViewset
from categories.api.router import router_categories
from posts.api.router import router_posts
from comments.api.router import router_comments


schema_view = get_schema_view(
   openapi.Info(
      title="Documentación API del Blog",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="naine@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   # permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # urls de la documentación
    path('docs/',schema_view.with_ui('swagger',cache_timeout=0),name='schema-swagger-ui'),
    path('redocs/',schema_view.with_ui('redoc',cache_timeout=0),name='schema-redoc'),
    path('api/',include('users.api.router')),
    # url categories
    path('api/',include(router_categories.urls)),
    # url posts
    path('api/',include(router_posts.urls)),
    # url comments
    path('api/',include(router_comments.urls)),
]
