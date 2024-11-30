### forms.py
from django import forms
from applications.producto.models import Provider

# Formulario para filtrar liquidaciones por proveedor y rango de fechas
class LiquidacionProviderForm(forms.Form):
    # Campo para seleccionar un proveedor desde un desplegable
    provider = forms.ModelChoiceField(
        required=True,
        queryset=Provider.objects.all(),  # Lista de todos los proveedores
        widget=forms.Select(
            attrs={
                'class': 'input-group-field',  # Clase CSS para el estilo
            }
        )
    )
    # Campo para seleccionar la fecha de inicio
    date_start = forms.DateField(
        required=True,
        widget=forms.DateInput(
            format='%Y-%m-%d',  # Formato de la fecha
            attrs={
                'type': 'date',  # Tipo de input como selector de fecha
                'class': 'input-group-field',
            },
        )
    )
    # Campo para seleccionar la fecha de fin
    date_end = forms.DateField(
        required=True,
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
                'class': 'input-group-field',
            },
        )
    )

# Formulario para generar un resumen de ventas basado en un rango de fechas
class ResumenVentasForm(forms.Form):
    date_start = forms.DateField(
        required=True,
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
                'class': 'input-group-field',
            },
        )
    )
    date_end = forms.DateField(
        required=True,
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
                'class': 'input-group-field',
            },
        )
    )
