from django.shortcuts import render

from servicio.models import CategoriaServicio


def home(request):
    return render(request, "servicio/home.html")


def categoriaservicio_list(request):
    categorias = CategoriaServicio.objects.all()
    return render(request, "servicio/categoriaservicio_list.html", {"categorias": categorias})
