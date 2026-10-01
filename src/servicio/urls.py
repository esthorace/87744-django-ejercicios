from django.urls import path

from servicio import views

app_name = "servicio"

urlpatterns = [
    path("", views.home, name="home"),
    path("categoria/list/", views.categoriaservicio_list, name="categoriaservicio_list"),
]
