from django.db import models


class CategoriaServicio(models.Model):
    nombre = models.CharField()
    descripcion = models.TextField()
