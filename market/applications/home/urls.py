### urls.py
from django.urls import path
from . import views

# URLs de la aplicación "home"
app_name = "home_app"

urlpatterns = [
    path(
        'panel/', 
        views.PanelHomeView.as_view(),  # Vista principal del panel
        name='index',
    ),
    path(
        'panel/admin/', 
        views.PanelAdminView.as_view(),  # Panel para administradores
        name='index-admin',
    ),
    path(
        'panel/admin-reporte/', 
        views.ReporteAdmin.as_view(),  # Reporte general de administradores
        name='admin-reporte',
    ),
    path(
        'panel/admin-liquidacion/', 
        views.ReporteLiquidacion.as_view(),  # Reporte de liquidaciones
        name='admin-liquidacion',
    ),
    path(
        'panel/admin-resumen-ventas/', 
        views.ReporteResumenVentas.as_view(),  # Reporte de resumen de ventas
        name='admin-resumen_ventas',
    ),
]