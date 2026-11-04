from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('paginas.urls')),
    path('articulos/', include('articulos.urls')),
    path('categorias/', include('categorias.urls')),
    path('autores/', include('autores.urls')),
    path('comentarios/', include('comentarios.urls')),
    path('contacto/', include('contacto.urls')),
]
