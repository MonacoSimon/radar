from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'