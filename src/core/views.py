from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def te_saludo(request):
    nombre = input("Nombre: ")
    return HttpResponse(f"<p>¡Hola {nombre}!</p>")


def home(request):
    lista_notas = [1, 10, 4, 7, 8, 5, 7]
    return render(request, "core/home.html", {"notas": lista_notas})
