from django.urls import path

from servicio.views import categoriaservicio_list

app_name = "servicio"

urlpatterns = [
    path("categoria/list/", categoriaservicio_list, name="categoria_list"),
]
