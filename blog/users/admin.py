from django.contrib import admin

# 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User

# decorador
@admin.register(User)
class userAdmin(BaseUserAdmin):
    pass
