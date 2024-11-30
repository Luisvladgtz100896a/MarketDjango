from django.db.models import Prefetch, F, FloatField, ExpressionWrapper  # Herramientas para optimizar consultas.
from applications.venta.models import Sale, SaleDetail  # Modelos relacionados con ventas y detalles de ventas.

def detalle_ventas_no_cerradas():
    # Recupera las ventas que aún no han sido cerradas.
    ventas = Sale.objects.ventas_no_cerradas()  # Obtiene las ventas no cerradas desde el administrador del modelo.
    consulta = ventas.prefetch_related(
        Prefetch(
            'detail_sale',  # Relación a prefetch en los detalles de venta.
            queryset=SaleDetail.objects.filter(sale__id__in=ventas).annotate(
                subtotal=ExpressionWrapper(  # Calcula el subtotal multiplicando precio por cantidad.
                    F('price_sale') * F('count'),
                    output_field=FloatField()  # Define el campo resultante como flotante.
                )
            )
        )
    )
    return consulta  # Devuelve las ventas con los detalles anotados.