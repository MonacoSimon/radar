from django.contrib import admin
from .models import Autor


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'activo', 'fecha_registro')
    list_filter = ('activo',)
    search_fields = ('nombre', 'apellido', 'email')