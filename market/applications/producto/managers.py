from datetime import timedelta
# Importaciones de Django
from django.db import models
from django.utils import timezone
from django.db.models import Q, F

class ProductManager(models.Manager):
    #Manager personalizado para el modelo Product"""

    def buscar_producto(self, kword, order):
        
        
        #Busca productos basados en una palabra clave y ordena los resultados
        #según el criterio especificado.
        
        # Filtra productos cuyo nombre o código de barras contenga la palabra clave
        consulta = self.filter(
            Q(name__icontains=kword) | Q(barcode=kword)
        )
        # Verifica el criterio de ordenamiento especificado
        if order == 'date':
            # Ordena los productos por fecha de creación (ascendente)
            return consulta.order_by('created')
        elif order == 'name':
            # Ordena los productos por nombre (ascendente)
            return consulta.order_by('name')
        elif order == 'stok':
            # Ordena los productos por cantidad en stock (ascendente)
            return consulta.order_by('count')
        else:
            # Ordena los productos por fecha de creación (descendente) como predeterminado
            return consulta.order_by('-created')
    
    def update_stok_ventas_producto(self, venta_id):
        
        #Incrementa el stock de los productos asociados a una venta específica.
        
        # Filtra los productos relacionados con una venta específica
        consulta = self.filter(
            product_sale__sale__id=venta_id
        )
        # Incrementa el stock de cada producto relacionado en la consulta
        consulta.update(count=(F('count') + 1))
    
    def productos_en_cero(self):
        """
        Retorna los productos cuyo stock es menor a 10.
        """
        # Filtra productos con stock menor a 10
        consulta = self.filter(
           count__lt=10
        )
        # Retorna la consulta con los productos filtrados
        return consulta
    
    def filtrar(self, **filters):
        """
        Filtra productos según múltiples criterios como rango de fechas, palabra clave,
        marca y proveedor, y ordena los resultados según el criterio especificado.
        """
        # Establece una fecha de inicio predeterminada si no se especifica
        if not filters['date_start']:
            filters['date_start'] = '2024-01-01'
        
        # Establece una fecha de fin predeterminada si no se especifica
        if not filters['date_end']:
            filters['date_end'] = timezone.now().date() + timedelta(1080)
        
        # Filtra productos dentro del rango de fechas especificado
        consulta = self.filter(
            due_date__range=(filters['date_start'], filters['date_end'])
        ).filter(
            # Filtra productos cuyo nombre o código de barras coincida con la palabra clave
            Q(name__icontains=filters['kword']) | Q(barcode=filters['kword'])
        ).filter(
            # Filtra productos por marca y proveedor
            marca__name__icontains=filters['marca'],
            provider__name__icontains=filters['provider'],
        )

        # Ordena los productos según el criterio especificado
        if filters['order'] == 'name':
            # Ordena por nombre (ascendente)
            return consulta.order_by('name')
        elif filters['order'] == 'stok':
            # Ordena por cantidad en stock (ascendente)
            return consulta.order_by('count')
        elif filters['order'] == 'num':
            # Ordena por número de ventas (descendente)
            return consulta.order_by('-num_sale')
        else:
            # Ordena por fecha de creación (descendente) como predeterminado
            return consulta.order_by('-created')
