from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from users.api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer

# permisos de usuario
from rest_framework.permissions import IsAuthenticated

# registrar usuarios
class RegisterView(APIView):
    def post(self,request):
        # utilizar el serializador

        # request.data: toda la información del usuario
        serializer = UserRegisterSerializer(data=request.data)
        # datos iguales al serializador guardar en db
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        # si tiene errores generar un http 400
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    # usuarios autenticados pueden realizar peticiones
    permission_classes = [IsAuthenticated]

    # obtener datos del usuario
    def get(self,request):
        serializer = UserSerializer(request.user)
        # retorna los datos del usuario
        return Response(serializer.data)

    # modificar datos del usuario
    def put(self,request):
        # obtener los datos por id
        user = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(user,request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    