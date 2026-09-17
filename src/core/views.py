from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def te_saludo(request):
    nombre = input("Nombre: ")
    return HttpResponse(f"<p>¡Hola {nombre}!</p>")


def home(request):
    lista_notas = [1, 10, 4, 7, 8, 5, 7]
    return render(request, "core/home.html", {"notas": lista_notas})


def ejercicio4(request):
    usuarios = [
        {"nombre": "juan", "email": "juan@django"},
        {"nombre": "santi", "email": "juan@django"},
        {"nombre": "agustín", "email": "juan@django"},
    ]
    return render(request, "core/ejercicio4.html", {"usuarios": usuarios})
