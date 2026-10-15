from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q, QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from ..forms import ClienteForm
from ..models import Cliente


class ClienteList(ListView):
    model = Cliente
    template_name = "servicio/cliente_list.html"
    context_object_name = "clientes"
    paginate_by = 10
    ordering = ("apellido", "nombre", "-pk")

    def get_queryset(self) -> QuerySet:
        clientes = super().get_queryset()
        busqueda = self.request.GET.get("busqueda", "").strip()

        if busqueda:
            clientes = clientes.filter(
                Q(nombre__icontains=busqueda) | Q(apellido__icontains=busqueda),
            )
        return clientes


class ClienteCreate(SuccessMessageMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "servicio/cliente_form.html"
    success_url = reverse_lazy("servicio:cliente_list")
    success_message = "Cliente creado correctamente."

    def form_invalid(self, form):
        messages.error(self.request, "No se pudo crear el cliente. Revisá los errores del formulario.")
        return super().form_invalid(form)


class ClienteDetail(DetailView):
    model = Cliente
    template_name = "servicio/cliente_detail.html"
    context_object_name = "cliente"


class ClienteUpdate(SuccessMessageMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "servicio/cliente_form.html"
    success_url = reverse_lazy("servicio:cliente_list")
    success_message = "Cliente actualizado correctamente."

    def form_invalid(self, form):
        messages.error(self.request, "No se pudo actualizar el cliente. Revisá los errores del formulario.")
        return super().form_invalid(form)


class ClienteDelete(DeleteView):
    model = Cliente
    template_name = "servicio/cliente_delete.html"
    context_object_name = "cliente"
    success_url = reverse_lazy("servicio:cliente_list")

    def delete(self, request, *args, **kwargs):
        cliente = self.get_object()
        messages.success(request, f"Cliente '{cliente}' eliminado correctamente.")
        return super().delete(request, *args, **kwargs)
