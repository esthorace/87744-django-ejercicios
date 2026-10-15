from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from ..forms import CategoriaServicioForm
from ..models import CategoriaServicio


def categoriaservicio_list(request: HttpRequest) -> HttpResponse:
    busqueda = request.GET.get("busqueda", "").strip()

    categorias = CategoriaServicio.objects.all()

    if busqueda:
        categorias = categorias.filter(nombre__contains=busqueda)
        """
        SELECT *
        FROM servicio_categoriaservicio
        WHERE nombre ILIKE '%busqueda%'
        """

    return render(request, "servicio/categoriaservicio_list.html", {"categorias": categorias})


def categoriaservicio_detail(request, pk):
    categoria = get_object_or_404(CategoriaServicio, pk=pk)
    return render(request, "servicio/categoriaservicio_detail.html", {"categoria": categoria})


def categoriaservicio_create(request):
    if request.method == "POST":
        form = CategoriaServicioForm(request.POST)
        if form.is_valid():
            categoria = form.save()
            messages.success(request, f"Categoría '{categoria.nombre}' creada correctamente.")
            return redirect("servicio:categoriaservicio_list")
        messages.error(request, "No se pudo crear la categoría. Revisá los errores del formulario.")
    else:
        form = CategoriaServicioForm()

    return render(request, "servicio/categoriaservicio_form.html", {"form": form})


def categoriaservicio_update(request, pk):
    categoria = get_object_or_404(CategoriaServicio, pk=pk)

    if request.method == "POST":
        form = CategoriaServicioForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria = form.save()
            messages.success(request, f"Categoría '{categoria.nombre}' actualizada correctamente.")
            return redirect("servicio:categoriaservicio_list")
        messages.error(
            request, "No se pudo actualizar la categoría. Revisá los errores del formulario."
        )
    else:
        form = CategoriaServicioForm(instance=categoria)

    return render(request, "servicio/categoriaservicio_form.html", {"form": form})


def categoriaservicio_delete(request, pk):
    categoria = get_object_or_404(CategoriaServicio, pk=pk)

    if request.method == "POST":
        nombre = categoria.nombre
        categoria.delete()
        messages.success(request, f"Categoría '{nombre}' eliminada correctamente.")
        return redirect("servicio:categoriaservicio_list")

    return render(request, "servicio/categoriaservicio_delete.html", {"categoria": categoria})
