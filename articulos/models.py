from django.db import models
from autores.models import Autor
from categorias.models import Categoria


class Articulo(models.Model):

    ESTADOS = [
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
        ('archivado', 'Archivado'),
    ]

    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(unique=True)
    contenido = models.TextField()
    imagen = models.ImageField(
        upload_to='articulos/',
        blank=True,
        null=True
    )
    estado = models.CharField(
        max_length=10,
        choices=ESTADOS,
        default='borrador'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    contador_visitas = models.PositiveIntegerField(default=0)

    autor = models.ForeignKey(
        Autor,
        on_delete=models.PROTECT,
        related_name='articulos'
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='articulos'
    )

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'