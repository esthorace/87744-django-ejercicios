from django.contrib import admin

from servicio.models import CategoriaServicio, Cliente, Servicio


@admin.register(CategoriaServicio)
class CategoriaServicioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion_corta")
    search_fields = ("nombre", "descripcion")
    ordering = ("nombre",)
    list_per_page = 25
    empty_value_display = "—"

    @admin.display(description="Descripción")
    def descripcion_corta(self, obj: CategoriaServicio) -> str:
        """Devuelve la descripción recortada para la vista de lista."""
        if not obj.descripcion:
            return "—"
        return obj.descripcion if len(obj.descripcion) <= 60 else f"{obj.descripcion[:57]}..."


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre_completo", "email", "telefono")
    list_display_links = ("nombre_completo",)
    list_filter = ("apellido",)
    search_fields = ("nombre", "apellido", "email", "telefono")
    ordering = ("apellido", "nombre")
    list_per_page = 25
    empty_value_display = "—"

    @admin.display(description="Nombre completo", ordering="nombre")
    def nombre_completo(self, obj: Cliente) -> str:
        """Muestra nombre y apellido como un solo enlace de detalle."""
        return str(obj)


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "cliente",
        "categoria",
        "presupuesto_formateado",
        "get_estado_servicio_display",
        "get_estado_pago_display",
        "fecha_creacion",
    )
    list_display_links = ("pk", "cliente")
    list_filter = ("estado_servicio", "estado_pago", "categoria", "fecha_creacion")
    search_fields = (
        "descripcion",
        "cliente__nombre",
        "cliente__apellido",
        "cliente__email",
        "categoria__nombre",
    )
    autocomplete_fields = ("categoria", "cliente")
    readonly_fields = ("fecha_creacion", "fecha_actualizacion")
    date_hierarchy = "fecha_creacion"
    list_select_related = ("categoria", "cliente")
    list_per_page = 25
    empty_value_display = "—"
    fieldsets = (
        (
            "Datos del servicio",
            {"fields": ("categoria", "cliente", "descripcion", "presupuesto")},
        ),
        (
            "Estado",
            {"fields": ("estado_servicio", "estado_pago")},
        ),
        (
            "Fechas",
            {"fields": ("fecha_creacion", "fecha_actualizacion")},
        ),
    )

    @admin.display(description="Presupuesto", ordering="presupuesto")
    def presupuesto_formateado(self, obj: Servicio) -> str:
        """Muestra el presupuesto con separador de miles y dos decimales."""
        return f"$ {obj.presupuesto:,.2f}"
