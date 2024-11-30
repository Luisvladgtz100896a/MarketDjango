# Archivo models.py
from django.db import models  # Importa el módulo de modelos de Django.
from django.conf import settings  # Importa la configuración del proyecto.
from model_utils.models import TimeStampedModel  # Clase base con campos de timestamp (creado/modificado).

# Modelo para representar los cierres de caja.
class CloseBox(TimeStampedModel):
    """
        Representa los cierres de caja.
    """
    date_close = models.DateTimeField(  # Fecha y hora del cierre de caja.
        'Fecha de Cierre',
    )
    count = models.PositiveIntegerField(  # Número de ventas cerradas.
        'Cantidad de ventas'
    )
    amount = models.DecimalField(  # Monto total de las ventas cerradas.
        'Monto total en ventas', 
        max_digits=10,  # Máximo de dígitos permitidos.
        decimal_places=2  # Número de decimales permitidos.
    )
    user = models.ForeignKey(  # Relación con el usuario que cerró la caja.
        settings.AUTH_USER_MODEL,  # Modelo de usuario definido en la configuración del proyecto.
        on_delete=models.CASCADE,  # Elimina el cierre si se elimina el usuario asociado.
        verbose_name='cajero',  # Nombre para mostrar en el administrador.
        related_name="close_user",  # Nombre para referenciar esta relación en consultas.
    )

    class Meta:
        verbose_name = 'Cierre Caja'  # Nombre singular para el modelo.
        verbose_name_plural = 'Cierres de Caja'  # Nombre plural para el modelo.

    def __str__(self):
        # Representación en texto del objeto.
        return str(self.user.full_name) + ' - ' + str(self.date_close)