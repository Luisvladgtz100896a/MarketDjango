### functions.py
from django.db.models import Prefetch, F, FloatField, ExpressionWrapper
from applications.venta.models import Sale, SaleDetail

# Función para obtener ventas y sus detalles dentro de un rango de fechas
# Incluye el cálculo del subtotal de cada detalle (precio por cantidad)
def detalle_resumen_ventas(date_start, date_end):
    if date_start and date_end:  # Verifica que ambas fechas sean válidas
        # Filtra las ventas en el rango de fechas especificado
        ventas = Sale.objects.ventas_en_fechas(date_start, date_end)
        # Recupera las ventas junto con su detalle (optimizado con prefetch_related)
        consulta = ventas.prefetch_related(
            Prefetch(
                'detail_sale',  # Relación hacia SaleDetail
                queryset=SaleDetail.objects.filter(sale__id__in=ventas).annotate(
                    subtotal=ExpressionWrapper(
                        F('price_sale') * F('count'),  # Calcula el subtotal por detalle
                        output_field=FloatField()  # Define el tipo de dato
                    )
                )
            )
        )
        return consulta
    else:
        return []