from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def te_saludo(request):
    nombre = input("Nombre: ")
    return HttpResponse(f"<p>¡Hola {nombre}!</p>")
