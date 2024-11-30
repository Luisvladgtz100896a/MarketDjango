# Importamos módulos necesarios
from model_utils.models import TimeStampedModel  # Modelo para fechas de creación y modificación automáticas
from django.db import models  # Módulos de Django para manejar modelos
from .managers import ProductManager  # Importamos un manager personalizado para el modelo Product

# Modelo Marca, para representar la marca de un producto
class Marca(TimeStampedModel):
    """
        Marca de un producto
    """
    name = models.CharField('Nombre', max_length=30)  # Campo para el nombre de la marca

    class Meta:
        verbose_name = 'Marca'  # Nombre en singular
        verbose_name_plural = 'Marcas'  # Nombre en plural

    def __str__(self):
        return self.name  # Retorna el nombre de la marca como su representación en cadena


# Modelo Provider, para representar al proveedor de un producto
class Provider(TimeStampedModel):
    """
        Proveedore de Producto
    """
    name = models.CharField('Razon Social', max_length=100)  # Nombre del proveedor (razón social)
    email = models.EmailField(blank=True, null=True)  # Correo electrónico del proveedor
    phone = models.CharField('Telefonos', max_length=40, blank=True)  # Teléfonos del proveedor
    web = models.URLField('Sitio Web', blank=True)  # Página web del proveedor

    class Meta:
        verbose_name = 'Proveedor'  # Nombre en singular
        verbose_name_plural = 'Proveedores'  # Nombre en plural

    def __str__(self):
        return self.name  # Retorna el nombre del proveedor como su representación en cadena


# Modelo Product, para representar los productos
class Product(TimeStampedModel):
    """
        Producto
    """
    # Opciones para las unidades de medida
    UNIT_CHOICES = (
        ('0', 'Kilogramos'),
        ('1', 'Litros'),
        ('2', 'Unidades'),
    )

    # Campos del modelo Product
    barcode = models.CharField(max_length=13, unique=True)  # Código de barras único del producto
    name = models.CharField('Nombre', max_length=40)  # Nombre del producto
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)  # Relación con el proveedor  (clave foránea)
    
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)  # Relación con la marca (clave foránea)
    due_date = models.DateField('Fecha de vencimiento', blank=True, null=True)  # Fecha de vencimiento del producto
    description = models.TextField('Descripción del producto', blank=True)  # Descripción del producto
    unit = models.CharField('Unidad de medida', max_length=1, choices=UNIT_CHOICES)  # Unidad de medida
    count = models.PositiveIntegerField('Cantidad en almacen', default=0)  # Cantidad disponible en el almacén
    purchase_price = models.DecimalField('Precio compra', max_digits=7, decimal_places=2)  # Precio de compra
    sale_price = models.DecimalField('Precio venta', max_digits=7, decimal_places=2)  # Precio de venta
    num_sale = models.PositiveIntegerField('Número de ventas', default=0)  # Número de veces que ha sido vendido
    anulate = models.BooleanField('Eliminado', default=False)  # Campo para marcar si el producto está eliminado

    # Manager personalizado para la búsqueda y filtrado de productos
    objects = ProductManager()

    class Meta:
        verbose_name = 'Producto'  # Nombre en singular
        verbose_name_plural = 'Productos'  # Nombre en plural

    def __str__(self):
        return self.name  # Retorna el nombre del producto como su representación en cadena
