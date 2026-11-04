from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('paginas.urls')),
    path('articulos/', include('articulos.urls')),
    path('categorias/', include('categorias.urls')),
    path('autores/', include('autores.urls')),
    path('comentarios/', include('comentarios.urls')),
    path('contacto/', include('contacto.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)