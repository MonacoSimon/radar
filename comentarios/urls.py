from django.urls import path
from . import views

app_name = 'comentarios'

urlpatterns = [
    path(
        'nuevo/<int:articulo_id>/',
        views.crear_comentario,
        name='crear'
    ),
]