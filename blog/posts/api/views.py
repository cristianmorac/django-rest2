from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from posts.api.serializers import PostSerializer

# permisos de usuario
from posts.api.permissions import IsAdminreadOnly
# filtros
from django_filters.rest_framework import DjangoFilterBackend

class PostApiViewSet(ModelViewSet):
    permission_classes = [IsAdminreadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)

    # filtro
    filter_backends = [DjangoFilterBackend]
    # filtrar por un campo en especifico
    filterset_fields = ['category','category__slug']