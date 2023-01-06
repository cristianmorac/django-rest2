from django.db import models

# modelo de usuario basico de django
from django.contrib.auth.models import AbstractUser

# clase que se sobrescribe del usuario
class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    # debe estar añadido o genera un error
    REQUIRED_FIELDS = []

