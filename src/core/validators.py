import re
from typing import Any

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ValidarTextoEspañol:
    """
    Valida longitud mínima y caracteres permitidos en español.
    Si `permitir_puntuacion=True`, admite comas, puntos, guiones y saltos de línea.
    """

    def __init__(
        self,
        min_longitud: int = 3,
        permitir_puntuacion: bool = False,
        mensaje: str | None = None,
    ):
        self.min_longitud = min_longitud
        self.permitir_puntuacion = permitir_puntuacion
        self.mensaje = mensaje

        if permitir_puntuacion:
            # Letras en español, números, espacios, saltos de línea y puntuación básica
            self.patron = r"^[a-zA-Z0-9áéíóúÁÉÍÓÚüÜñÑ\s.,;:()\"'\n\r]+$"
        else:
            # Solo letras en español y espacios
            self.patron = r"^[a-zA-záéíóúÁÉÍÓÚüÜñÑ\s]+$"

    def __call__(self, valor: str) -> None:
        texto = valor.strip() if valor else ""

        if len(texto) < self.min_longitud:
            msg = self.mensaje or f"El texto debe contener al menos {self.min_longitud} caracteres."
            raise ValidationError(msg)

        if not re.match(self.patron, texto):
            msg = self.mensaje or (
                "El texto contiene caracteres no válidos."
                if self.permitir_puntuacion
                else "El texto solo puede contener letras, acentos y espacios."
            )
            raise ValidationError(msg)


@deconstructible
class ValidarTelefono:
    """Valida formatos telefónicos internacionales y locales simples (ej. +54911223344, 2615551234)."""

    def __init__(self, mensaje: str | None = None):
        self.mensaje = (
            mensaje
            or "El número de teléfono debe contener entre 7 y 15 dígitos y opcionalmente el prefijo '+'."
        )
        self.patron = r"^\+?[0-9]{7,15}$"

    def __call__(self, valor: str) -> None:
        texto = valor.strip() if valor else ""
        # Remueve espacios y guiones intermedios para la verificación
        texto_limpio = re.sub(r"[\s\-]", "", texto)

        if not re.match(self.patron, texto_limpio):
            raise ValidationError(self.mensaje)
