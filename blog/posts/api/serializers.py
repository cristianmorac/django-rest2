from rest_framework import serializers
from posts.models import Post
# importar serializadores
from users.api.serializers import UserSerializer
from categories.api.serializers import CategorySerializer

class PostSerializer(serializers.ModelSerializer):
    # obtener la información del usuario
    user = UserSerializer()
    # obtener la información de categoria
    category = CategorySerializer()
    class Meta:
        model = Post
        fields = ['title','content','slug','miniature','created_at','published','user','category']