from django.views.generic import ListView

from ..models import Cliente


class ClienteList(ListView):
    model = Cliente
    template_name = "servicio/cliente_list.html"
    context_object_name = "clientes"
