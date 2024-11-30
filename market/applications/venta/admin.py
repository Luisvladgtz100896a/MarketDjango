from django.contrib import admin
# Importamos los modelos relacionados con la venta
from .models import Sale, SaleDetail

# Configuración del administrador para el modelo Sale
class SaleAdmin(admin.ModelAdmin):
    list_display = (
        'date_sale',  # Muestra la fecha de la venta
        'count',  # Muestra la cantidad de productos vendidos
        'amount',  # Muestra el monto total de la venta
        'user',  # Muestra el usuario que realizó la venta
        'close',  # Muestra si la venta está cerrada
        'anulate',  # Muestra si la venta está anulada
    )
    # Permite filtrar las ventas por tipo de factura, tipo de pago, si está anulada o el usuario que la realizó
    list_filter = ('type_invoce', 'type_payment', 'anulate', 'user', )

# Configuración del administrador para el modelo SaleDetail
class SaleDetailAdmin(admin.ModelAdmin):
    list_display = (
        'product',  # Muestra el producto relacionado con el detalle de la venta
        'sale',  # Muestra la venta relacionada con el detalle
        'count',  # Muestra la cantidad de productos en el detalle
        'anulate',  # Muestra si el detalle está anulado
    )
    # Permite buscar detalles de ventas por el nombre del producto
    search_fields = ('product__name',)

# Registramos los modelos en el panel de administración
admin.site.register(Sale, SaleAdmin)
admin.site.register(SaleDetail, SaleDetailAdmin)
