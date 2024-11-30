from django import forms
# Importamos el modelo Sale
from .models import Sale

# Formulario para procesar una venta (registro de productos)
class VentaForm(forms.Form):
    # Campo para el código de barras del producto
    barcode = forms.CharField(
        required=True,  # El código de barras es obligatorio
        widget=forms.TextInput(
            attrs = {
                'placeholder': 'Codigo de barras',  # Placeholder en el campo
                'class': 'input-group-field',  # Clase CSS para el estilo
            }
        )
    )
    # Campo para la cantidad de productos que se desean comprar
    count = forms.IntegerField(
        min_value=1,  # La cantidad mínima es 1
        widget=forms.NumberInput(
            attrs = {
                'value': '1',  # Valor inicial del campo
                'class': 'input-group-field',  # Clase CSS para el estilo
            }
        )
    )
    # Validación personalizada para la cantidad
    def clean_count(self):
        count = self.cleaned_data['count']
        if count < 1:
            raise forms.ValidationError('Ingrese una cantidad mayor a cero')  # Error si la cantidad es menor a 1
        return count

# Formulario para procesar el tipo de pago y tipo de factura de la venta
class VentaVoucherForm(forms.Form):
    # Campo para seleccionar el tipo de pago
    type_payment = forms.ChoiceField(
        required=False,  # No es obligatorio
        choices=Sale.TIPO_PAYMENT_CHOICES,  # Opciones definidas en el modelo Sale
        widget=forms.Select(
            attrs = {
                'class': 'input-group-field',  # Clase CSS para el estilo
            }
        )
    )
    # Campo para seleccionar el tipo de factura
    type_invoce = forms.ChoiceField(
        required=False,  # No es obligatorio
        choices=Sale.TIPO_INVOCE_CHOICES,  # Opciones definidas en el modelo Sale
        widget=forms.Select(
            attrs = {
                'class': 'input-group-field',  # Clase CSS para el estilo
            }
        )
    )
