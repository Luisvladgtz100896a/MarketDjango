# Django
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    View,
)
# Importaciones locales
from applications.venta.models import SaleDetail
from applications.users.mixins import AlmacenPermisoMixin
from .models import Product
from .forms import ProductForm
from applications.utils import render_to_pdf
from django.contrib.auth.mixins import LoginRequiredMixin

# Vista para listar productos
class ProductListView(AlmacenPermisoMixin, ListView):
    template_name = 'producto/lista.html'
    context_object_name = 'productos'

    def get_queryset(self):
        # Obtiene los parámetros de búsqueda y ordenamiento desde el request
        kword = self.request.GET.get("kword", '')  # Palabra clave para buscar productos
        order = self.request.GET.get("order", '')  # Criterio de ordenamiento
        # Llama al método personalizado del modelo para filtrar productos
        queryset = Product.objects.buscar_producto(kword, order)
        return queryset


# Vista para crear un nuevo producto
class ProductCreateView(AlmacenPermisoMixin, CreateView):
    template_name = "producto/form_producto.html"  # Plantilla que se usara
    form_class = ProductForm  # Formulario asociado al modelo
    success_url = reverse_lazy('producto_app:producto-lista')  # Redirige despues de crear un producto


# Vista para actualizar un producto existente
class ProductUpdateView(AlmacenPermisoMixin, UpdateView):
    template_name = "producto/form_producto.html"  # Plantilla que se usará
    model = Product  # Modelo asociado
    form_class = ProductForm  # Formulario asociado
    success_url = reverse_lazy('producto_app:producto-lista')  # Redirige después de actualizar


# Vista para eliminar un producto
class ProductDeleteView(AlmacenPermisoMixin, DeleteView):
    template_name = "producto/delete.html"  # Plantilla que se usará
    model = Product  # Modelo asociado
    success_url = reverse_lazy('producto_app:producto-lista')  # Redirige después de eliminar


# Vista para mostrar detalles de un producto
class ProductDetailView(AlmacenPermisoMixin, DetailView):
    template_name = "producto/detail.html"  # Plantilla que se usará
    model = Product  # Modelo asociado

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtiene las ventas del producto en el mes actual
        context["ventas_mes"] = SaleDetail.objects.ventas_mes_producto(
            self.kwargs['pk']  # Identificador del producto
        )
        return context


# Vista para generar un PDF con los detalles del producto
class ProductDetailViewPdf(AlmacenPermisoMixin, View):

    def get(self, request, *args, **kwargs):
        # Obtiene el producto por su ID
        producto = Product.objects.get(id=self.kwargs['pk'])
        # Prepara los datos para renderizar en el PDF
        data = {
            'product': producto,
            'ventas_mes': SaleDetail.objects.ventas_mes_producto(self.kwargs['pk'])
        }
        # Genera el PDF usando una función utilitaria
        pdf = render_to_pdf('producto/detail-print.html', data)
        # Devuelve el PDF como respuesta HTTP
        return HttpResponse(pdf, content_type='application/pdf')


# Vista para filtrar productos con múltiples criterios
class FiltrosProductListView(AlmacenPermisoMixin, ListView):
    template_name = "producto/filtros.html"  # Plantilla que se usará
    context_object_name = 'productos'  # Nombre del contexto para los productos

    def get_queryset(self):
        # Llama al método personalizado para filtrar productos
        queryset = Product.objects.filtrar(
            kword=self.request.GET.get("kword", ''),  # Palabra clave para buscar
            date_start=self.request.GET.get("date_start", ''),  # Fecha de inicio
            date_end=self.request.GET.get("date_end", ''),  # Fecha de fin
            provider=self.request.GET.get("provider", ''),  # Proveedor
            marca=self.request.GET.get("marca", ''),  # Marca
            order=self.request.GET.get("order", ''),  # Criterio de ordenamiento
        )
        return queryset
