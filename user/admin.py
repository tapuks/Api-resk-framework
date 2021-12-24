from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from user.models import User


@admin.register(User)
class UserAdministrador(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username',)}),
        ('Redes sociales', {'fields': ('instagram',)}),
    )
