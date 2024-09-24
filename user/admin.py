from django.contrib import admin
from user.models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'is_authenticated')