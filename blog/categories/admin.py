from django.contrib import admin
from categories.models import Category

@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    # información que se muestra en el panel de admin
    list_display = ['title','published']
