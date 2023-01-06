from rest_framework.permissions import BasePermission
from comments.models import Comment

class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            id_comment = view.kwargs['pk']
            # muestra la información del comentario del id 
            comment = Comment.objects.get(pk=id_comment)

            # obteniendo el id del usuario que esta ejecutando la petición de actualizar o eliminar 
            id_user = request.user.pk
            # el id del usuario que ha creado el comanetario
            id_user_comment = comment.user_id

            if id_user == id_user_comment:
                return True
            return False
