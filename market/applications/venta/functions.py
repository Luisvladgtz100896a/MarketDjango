from django.utils import timezone  # Para manejar fechas y horas
from django.db.models import Prefetch  # Para optimizar consultas

# Importamos el modelo Product (producto)
from applications.producto.models import Product
# Importamos los modelos relacionados con la venta
from .models import Sale, SaleDetail, CarShop

# Función para procesar una venta
def procesar_venta(self, **params_venta):
    # Recupera la lista de productos en el carrito de compras
    productos_en_car = CarShop.objects.all()
    
    # Si hay productos en el carrito
    if productos_en_car.count() > 0:
        
        # Crea una nueva venta con los datos proporcionados
        venta = Sale.objects.create(
            date_sale=timezone.now(),  # Establece la fecha de la venta como la hora actual
            count=0,  # Inicializa la cantidad de productos vendidos
            amount=0,  # Inicializa el monto total de la venta
            type_invoce=params_venta['type_invoce'],  # Tipo de factura
            type_payment=params_venta['type_payment'],  # Tipo de pago
            user=params_venta['user'],  # Usuario que realiza la venta
        )
        
        ventas_detalle = []  # Lista para almacenar los detalles de la venta
        productos_en_venta = []  # Lista para almacenar los productos actualizados
        
        # Itera sobre los productos en el carrito de compras
        for producto_car in productos_en_car:
            # Crea un detalle de venta para cada producto
            venta_detalle = SaleDetail(
                product=producto_car.product,  # Producto asociado
                sale=venta,  # Venta asociada
                count=producto_car.count,  # Cantidad del producto
                price_purchase=producto_car.product.purchase_price,  # Precio de compra del producto
                price_sale=producto_car.product.sale_price,  # Precio de venta del producto
                tax=0.18,  # Impuesto fijo del 18%
            )
            
            # Actualiza el stock de producto en cada iteración
            producto = producto_car.product
            producto.count = producto.count - producto_car.count  # Resta la cantidad del carrito al stock
            producto.num_sale = producto.num_sale + producto_car.count  # Aumenta el número de ventas

            # Añade el detalle de la venta y el producto actualizado a las listas
            ventas_detalle.append(venta_detalle)
            productos_en_venta.append(producto)
            
            # Actualiza la cantidad total de productos vendidos y el monto de la venta
            venta.count = venta.count + producto_car.count
            venta.amount = venta.amount + producto_car.count * producto_car.product.sale_price

        # Guarda la venta
        venta.save()
        
        # Crea todos los detalles de la venta de una vez con un solo query
        SaleDetail.objects.bulk_create(ventas_detalle)
        
        # Actualiza el stock de los productos con un solo query
        Product.objects.bulk_update(productos_en_venta, ['count', 'num_sale'])
        
        # Elimina los productos del carrito de compras una vez procesada la venta
        productos_en_car.delete()
        
        # Retorna la venta procesada
        return venta
    else:
        # Si no hay productos en el carrito, retorna None
        return None
