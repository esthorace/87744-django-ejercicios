import re

from django import forms

from .models import CategoriaServicio, Cliente


class CategoriaServicioForm(forms.ModelForm):
    class Meta:
        model = CategoriaServicio
        fields = "__all__"


def clean_nombre(self) -> str:
    nombre = self.cleaned_data.get("nombre", "")

    # Reemplaza múltiples espacios por uno solo y remueve espacios en los bordes
    nombre = re.sub(r"\s+", " ", nombre.strip())

    # Validación de longitud
    if len(nombre) < 3:
        raise forms.ValidationError("El nombre debe contener al menos 3 caracteres.")

    # Patron: solo letras en español y espacios sencillos
    patron = r"^[a-zA-záéíóúÁÉÍÓÚüÜñÑ ]+$"
    if not re.match(patron, nombre):
        raise forms.ValidationError(
            "El nombre solo puede contener letras, acentos y espacios, sin números ni caracteres especiales."
        )

    return nombre


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
