from django.db import models


class CategoriaServicio(models.Model):
    nombre = models.CharField(unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "Categoría de Servicio"
        verbose_name_plural = "Categorías de Servicio"
