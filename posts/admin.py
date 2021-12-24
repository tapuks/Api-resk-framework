from django.contrib import admin

# Register your models here.
from posts.models import Post

# REGISTRAMOS EL MODELO Y LE DECIMOS LOS CAMPOS QUE SE VEAN EN EL PANEL DE ADMINISTRADOR
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
