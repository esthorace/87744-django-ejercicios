from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(
            attrs={
                "id": "username",
                "autocomplete": "username",
                "autofocus": True,
            }
        ),
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={
                "id": "username",
                "autocomplete": "current-password",
            }
        ),
    )
    error_messages = {
        "invalid_login": "Por favor ingrese un nombre de usuario y contraseña correctos."
    }
