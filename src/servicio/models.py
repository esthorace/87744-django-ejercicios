from django.db import models


class CategoriaServicio(models.Model):
    nombre = models.CharField(unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "Categoría de Servicio"
        verbose_name_plural = "Categorías de Servicio"


class Cliente(models.Model):
    nombre = models.CharField()
    apellido = models.CharField()
    email = models.EmailField(unique=True, blank=True, null=True)
    telefono = models.CharField(unique=True)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
