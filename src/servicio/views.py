from django.shortcuts import redirect, render

from .forms import CategoriaServicioForm
from .models import CategoriaServicio


def home(request):
    return render(request, "servicio/home.html")


def categoriaservicio_list(request):
    categorias = CategoriaServicio.objects.all()
    return render(request, "servicio/categoriaservicio_list.html", {"categorias": categorias})


def categoriaservicio_create(request):
    if request.method == "POST":
        form = CategoriaServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("servicio:categoriaservicio_list")
    else:
        form = CategoriaServicioForm()

    return render(request, "servicio/categoriaservicio_form.html", {"form": form})
