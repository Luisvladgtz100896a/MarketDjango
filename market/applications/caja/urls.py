# Archivo urls.py
from django.urls import path  # Importa la función para definir rutas.
from . import views  # Importa las vistas desde el módulo actual.

app_name = "caja_app"  # Define un namespace para las rutas de esta aplicación.

urlpatterns = [
    path(
        'cierre-caja/index/',  # Ruta para acceder al reporte de cierre de caja.
        views.ReporteCierreCajaView.as_view(),  # Asocia la vista basada en clases correspondiente.
        name='caja-index',  # Nombre para referenciar esta ruta.
    ),
    path(
        'cierre-caja/cerrar/',  # Ruta para procesar el cierre de caja.
        views.ProcesoCerrarCajaView.as_view(),  # Asocia la vista basada en clases correspondiente.
        name='caja-cerrar',  # Nombre para referenciar esta ruta.
    ),
]