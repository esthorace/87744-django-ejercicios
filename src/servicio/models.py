from django.core.validators import MinValueValidator
from django.db import models

from core.validators import ValidarTelefono, ValidarTextoEspañol


class CategoriaServicio(models.Model):
    nombre = models.CharField(
        unique=True,
        validators=[ValidarTextoEspañol()],
    )
    descripcion = models.TextField(
        blank=True,
        validators=[
            ValidarTextoEspañol(min_longitud=10, permitir_puntuacion=True),
        ],
    )

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "Categoría de Servicio"
        verbose_name_plural = "Categorías de Servicio"


class Cliente(models.Model):
    nombre = models.CharField(validators=[ValidarTextoEspañol()])
    apellido = models.CharField(validators=[ValidarTextoEspañol()])
    email = models.EmailField(unique=True, blank=True, null=True)
    telefono = models.CharField(unique=True, validators=[ValidarTelefono()])

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def clean(self):
        super().clean()
        if self.nombre:
            self.nombre = self.nombre.strip()


class Servicio(models.Model):
    class EstadoServicio(models.TextChoices):
        PENDIENTE = "PENDIENTE", "Pendiente"
        EN_PROCESO = "EN_PROCESO", "En Proceso"
        COMPLETADO = "COMPLETADO", "Completado"
        CANCELADO = "CANCELADO", "Cancelado"

    class EstadoPago(models.TextChoices):
        PENDIENTE = "PENDIENTE", "Pendiente"
        PARCIAL = "PARCIAL", "Pago Parcial"
        PAGADO = "PAGADO", "Pagado"
        REEMBOLSADO = "REEMBOLSADO", "Reembolsado"

    categoria = models.ForeignKey(
        "CategoriaServicio",
        on_delete=models.PROTECT,
        related_name="servicios",
    )
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name="servicios",
    )
    descripcion = models.TextField(
        help_text="Descripción detallada del trabajo a realizar",
        validators=[ValidarTextoEspañol(min_longitud=10, permitir_puntuacion=True)],
    )
    presupuesto = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="Monto acordado",
    )
    estado_servicio = models.CharField(
        max_length=20,
        choices=EstadoServicio.choices,
        default=EstadoServicio.PENDIENTE,
    )
    estado_pago = models.CharField(
        max_length=20,
        choices=EstadoPago.choices,
        default=EstadoPago.PENDIENTE,
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ("-fecha_creacion",)

    def __str__(self) -> str:
        return f"Servicio #{self.pk} - {self.cliente} ({self.get_estado_servicio_display()})"  # type:ignore
