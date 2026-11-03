from django.db import models
from articulos.models import Articulo


class Comentario(models.Model):

    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
    ]

    contenido = models.TextField()
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    estado = models.CharField(
        max_length=10,
        choices=ESTADOS,
        default='pendiente'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    votos_favoritos = models.PositiveIntegerField(default=0)

    articulo = models.ForeignKey(
        Articulo,
        on_delete=models.CASCADE,
        related_name='comentarios'
    )

    def __str__(self):
        return f"Comentario de {self.nombre} en {self.articulo}"

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'