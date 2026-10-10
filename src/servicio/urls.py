from django.urls import path
from django.views.generic import TemplateView

from .views import *

app_name = "servicio"

urlpatterns = [
    path("", TemplateView.as_view(template_name="servicio/home.html"), name="home"),
    path("categoria/list/", categoriaservicio_list, name="categoriaservicio_list"),
    path("categoria/create/", categoriaservicio_create, name="categoriaservicio_create"),
    path("categoria/<int:pk>/", categoriaservicio_detail, name="categoriaservicio_detail"),
    path("categoria/<int:pk>/update/", categoriaservicio_update, name="categoriaservicio_update"),
    path("categoria/<int:pk>/delete/", categoriaservicio_delete, name="categoriaservicio_delete"),
    path("cliente/list/", ClienteList.as_view(), name="cliente_list"),
    path("cliente/create/", ClienteCreate.as_view(), name="cliente_create"),
    path("cliente/<int:pk>/", ClienteDetail.as_view(), name="cliente_detail"),
    path("cliente/<int:pk>/update/", ClienteUpdate.as_view(), name="cliente_update"),
    path("cliente/<int:pk>/delete/", ClienteDelete.as_view(), name="cliente_delete"),
]
