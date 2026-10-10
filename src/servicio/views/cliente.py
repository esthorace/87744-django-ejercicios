from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from ..forms import ClienteForm
from ..models import Cliente


class ClienteList(ListView):
    model = Cliente
    template_name = "servicio/cliente_list.html"
    context_object_name = "clientes"


class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "servicio/cliente_form.html"
    success_url = reverse_lazy("servicio:cliente_list")


class ClienteDetail(DetailView):
    model = Cliente
    template_name = "servicio/cliente_detail.html"
    context_object_name = "cliente"


class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "servicio/cliente_form.html"
    success_url = reverse_lazy("servicio:cliente_list")


class ClienteDelete(DeleteView):
    model = Cliente
    template_name = "servicio/cliente_delete.html"
    context_object_name = "cliente"
    success_url = reverse_lazy("servicio:cliente_list")
