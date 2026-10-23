from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.messages.api import success
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from core.forms import CustomLoginForm


def te_saludo(request):
    nombre = input("Nombre: ")
    return HttpResponse(f"<p>¡Hola {nombre}!</p>")


def home(request):
    lista_notas = [1, 10, 4, 7, 8, 5, 7]
    return render(request, "core/home.html", {"notas": lista_notas})


def login_view(request: HttpRequest) -> HttpResponse:
    error = None

    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Acceso correcto")
            return redirect("servicio:home")

        error = "Usuario o contraseña incorrectos."

    return render(request, "core/login.html", {"error": error})


class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = "core/login.html"
    form_class = CustomLoginForm
    success_message = "Acceso correcto"

    def get_success_url(self):
        return reverse_lazy("servicio:home")


# def logout_view(request: HttpRequest) -> HttpResponse:
#     # El cierre de sesión solo se ejecuta por POST (formulario del navbar).
#     if request.method == "POST":
#         logout(request)
#         messages.success(request, "Sesión cerrada")
#         # Redirige para que recargar la página no reenvíe el formulario.
#         return redirect("core:logout")

#     # Un usuario con sesión activa no debe ver la pantalla de despedida.
#     if request.user.is_authenticated:
#         return redirect("core:home")

#     return render(request, "core/logout.html")


# class LogoutView(auth_views.LogoutView):
#     """Cierra sesión (solo POST) y redirige a la pantalla de despedida."""

#     next_page = reverse_lazy("core:logout_done")

#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         # logout() ya vació la sesión; el mensaje va a una sesión nueva.
#         messages.success(request, "Sesión cerrada")
#         return response


# class LogoutDoneView(TemplateView):
#     """Pantalla de despedida: solo para usuarios sin sesión."""

#     template_name = "core/logout.html"

#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect("core:home")
#         return super().dispatch(request, *args, **kwargs)


def ejercicio_4(request):
    usuarios = [
        {"nombre": "juan", "email": "juan@django"},
        {"nombre": "santi", "email": "juan@django"},
        {"nombre": "agustín", "email": "juan@django"},
    ]
    return render(request, "core/ejercicio4.html", {"usuarios": usuarios})
