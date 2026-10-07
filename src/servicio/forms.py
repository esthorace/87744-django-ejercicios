from django import forms

from .models import CategoriaServicio


class CategoriaServicioForm(forms.ModelForm):
    class Meta:
        model = CategoriaServicio
        fields = "__all__"
