from django.shortcuts import get_object_or_404, redirect, render

from .forms import CategoriaServicioForm
from .models import CategoriaServicio


def home(request):
    return render(request, "servicio/home.html")


def categoriaservicio_list(request):
    categorias = CategoriaServicio.objects.all()
    return render(request, "servicio/categoriaservicio_list.html", {"categorias": categorias})


def categoriaservicio_detail(request, pk):
    categoria = get_object_or_404(CategoriaServicio, pk=pk)
    return render(request, "servicio/categoriaservicio_detail.html", {"categoria": categoria})


def categoriaservicio_create(request):
    if request.method == "POST":
        form = CategoriaServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("servicio:categoriaservicio_list")
    else:
        form = CategoriaServicioForm()

    return render(request, "servicio/categoriaservicio_form.html", {"form": form})


def categoriaservicio_update(request, pk):
    categoria = get_object_or_404(CategoriaServicio, pk=pk)

    if request.method == "POST":
        form = CategoriaServicioForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect("servicio:categoriaservicio_list")
    else:
        form = CategoriaServicioForm(instance=categoria)

    return render(request, "servicio/categoriaservicio_form.html", {"form": form})


def categoriaservicio_delete(request, pk):
    categoria = get_object_or_404(CategoriaServicio, pk=pk)

    if request.method == "POST":
        categoria.delete()
        return redirect("servicio:categoriaservicio_list")

    return render(request, "servicio/categoriaservicio_delete.html", {"categoria": categoria})
