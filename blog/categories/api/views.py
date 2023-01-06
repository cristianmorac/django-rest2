from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsAdminOrReadOnly

#django-filters
from django_filters.rest_framework import DjangoFilterBackend
 
class CategoryApiViewSet(ModelViewSet):
    # permiso personalizado 
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    # queryset = Category.objects.all()
    # filter
    queryset = Category.objects.filter(published=True)
    # relizar la busqueda por otro parametro
    lookup_field = 'slug'
    #django-filters
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['published','title']