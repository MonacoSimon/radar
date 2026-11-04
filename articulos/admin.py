from django.contrib import admin
from .models import Articulo


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'autor',
        'categoria',
        'estado',
        'fecha_creacion',
        'fecha_publicacion'
    )

    list_filter = ('estado', 'categoria', 'fecha_creacion')

    search_fields = (
        'titulo',
        'subtitulo',
        'contenido',
        'autor__nombre',
        'autor__apellido'
    )

    prepopulated_fields = {'slug': ('titulo',)}

    date_hierarchy = 'fecha_creacion'