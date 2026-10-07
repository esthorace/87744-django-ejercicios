from django.urls import path

from .views import (
    categoriaservicio_create,
    categoriaservicio_detail,
    categoriaservicio_list,
    home,
)

app_name = "servicio"

urlpatterns = [
    path("", home, name="home"),
    path("categoria/list/", categoriaservicio_list, name="categoriaservicio_list"),
    path("categoria/create/", categoriaservicio_create, name="categoriaservicio_create"),
    path(
        "categoria/<int:pk>/",
        categoriaservicio_detail,
        name="categoriaservicio_detail",
    ),
]
