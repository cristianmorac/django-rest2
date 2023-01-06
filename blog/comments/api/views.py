from rest_framework.viewsets import ModelViewSet
from comments.api.serializers import CommentSerializer

# importar el modelo
from comments.models import Comment

# importar filtro rest
from rest_framework.filters import OrderingFilter

# djangofilterbackend
from django_filters.rest_framework import DjangoFilterBackend

# permiso personalizado
from comments.api.permissions import IsOwnerOrReadAndCreateOnly

class CommentApiViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [OrderingFilter,DjangoFilterBackend]
    # campo a ordenar de maenra descendente
    ordering = ['-created_at']
    filterset_fields = ['post']