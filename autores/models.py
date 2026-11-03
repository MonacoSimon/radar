from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    biografia = models.TextField()
    foto_perfil = models.ImageField(
        upload_to='autores/',
        blank=True,
        null=True
    )
    activo = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        ordering = ['apellido', 'nombre']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'