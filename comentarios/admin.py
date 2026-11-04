from django.contrib import admin
from .models import Comentario


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'articulo',
        'estado',
        'fecha_creacion',
        'votos_favoritos'
    )

    list_filter = ('estado', 'fecha_creacion')

    search_fields = (
        'nombre',
        'email',
        'contenido',
        'articulo__titulo'
    )