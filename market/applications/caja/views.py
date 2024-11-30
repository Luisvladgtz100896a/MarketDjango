# django
from django.utils import timezone  # Para trabajar con fechas y horas.
from django.shortcuts import render  # Para renderizar plantillas HTML.
from django.http import HttpResponseRedirect  # Para redireccionar a otra URL después de una acción.
from django.urls import reverse_lazy, reverse  # Para generar URLs dinámicas.
from django.views.generic import (  # Clases genéricas de vistas en Django.
    View,  # Vista base para manejo personalizado de métodos HTTP (GET, POST, etc.).
    TemplateView  # Vista genérica basada en plantillas.
)

# Importaciones específicas de la aplicación
from applications.venta.models import Sale, SaleDetail  # Modelos relacionados con ventas.
from applications.users.mixins import VentasPermisoMixin  # Mixin para verificar permisos relacionados con ventas.
from .models import CloseBox  # Modelo para representar el cierre de caja.
from .functions import detalle_ventas_no_cerradas  # Función personalizada para obtener detalles de ventas no cerradas.

# Vista para generar un reporte del cierre de caja.
class ReporteCierreCajaView(VentasPermisoMixin, TemplateView):
    template_name = 'caja/index.html'  # Especifica la plantilla HTML a usar.

    def get_context_data(self, **kwargs):
        # Obtiene el contexto para renderizar la plantilla.
        context = super().get_context_data(**kwargs)  # Llama al método original para obtener el contexto base.
        
        context["ventas_dia"] = detalle_ventas_no_cerradas  # Añade detalles de las ventas no cerradas al contexto.
        
        context["total_vendido"] = Sale.objects.total_ventas_dia()  # Calcula el total de ventas realizadas hoy.
        
        context["total_anulado"] = Sale.objects.total_ventas_anuladas_dia()  # Calcula el total de ventas anuladas hoy.
        
        context["num_ventas_hoy"] = Sale.objects.ventas_no_cerradas().count()  # Cuenta el número de ventas no cerradas hoy.
        return context  # Devuelve el contexto actualizado.

# Vista para procesar el cierre de caja.
class ProcesoCerrarCajaView(VentasPermisoMixin, View):

    def post(self, request, *args, **kwargs):
        # Procesa la lógica para cerrar las ventas.
        num_cerradas, total = Sale.objects.cerrar_ventas()  # Cierra las ventas y obtiene el número de ventas cerradas y el total vendido.
        if num_cerradas > 0:  # Verifica si hay ventas cerradas para registrar el cierre de caja.
            CloseBox.objects.create(  # Crea un registro del cierre de caja en la base de datos.
                date_close=timezone.now(),  # Fecha y hora del cierre.
                count=num_cerradas,  # Número de ventas cerradas.
                amount=total,  # Monto total de las ventas cerradas.
                user=self.request.user  # Usuario que realizó el cierre de caja.
            )
        
        return HttpResponseRedirect(  # Redirecciona a la página principal de caja después de cerrar las ventas.
            reverse(
                'caja_app:caja-index'  # Genera la URL dinámica de la vista principal de caja.
            )
        )
