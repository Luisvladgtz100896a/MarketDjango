# Importamos las vistas desde el archivo views.py
from django.urls import path
from . import views

# Definimos el nombre de la aplicación para las rutas
app_name = "producto_app"

# Lista de rutas (URLs) que corresponden a vistas específicas de la aplicación
urlpatterns = [
    # Ruta para listar los productos (usando la vista ProductListView)
    path(
        'producto/lista/', 
        views.ProductListView.as_view(),  # Vista basada en clase
        name='producto-lista',  # Nombre de la ruta
    ),
    
    # Ruta para agregar un nuevo producto (usando la vista ProductCreateView)
    path(
        'producto/agregar/', 
        views.ProductCreateView.as_view(),
        name='producto-add',  # Nombre de la ruta
    ),
    
    # Ruta para actualizar un producto existente, con un parámetro 'pk' para identificar el producto (usando la vista ProductUpdateView)
    path(
        'producto/agregar/<pk>/', 
        views.ProductUpdateView.as_view(),
        name='producto-update',  # Nombre de la ruta
    ),
    
    # Ruta para eliminar un producto, con un parámetro 'pk' para identificar el producto (usando la vista ProductDeleteView)
    path(
        'producto/eliminar/<pk>/', 
        views.ProductDeleteView.as_view(),
        name='producto-delete',  # Nombre de la ruta
    ),
    
    # Ruta para ver los detalles de un producto, con un parámetro 'pk' para identificar el producto (usando la vista ProductDetailView)
    path(
        'producto/detalle/<pk>/', 
        views.ProductDetailView.as_view(),
        name='producto-detail',  # Nombre de la ruta
    ),
    
    # Ruta para generar e imprimir los detalles de un producto en PDF, con un parámetro 'pk' para identificar el producto (usando la vista ProductDetailViewPdf)
    path(
        'producto/detalle/print/<pk>/', 
        views.ProductDetailViewPdf.as_view(),
        name='producto-detail_print',  # Nombre de la ruta
    ),
    
    # Ruta para aplicar filtros a los productos (usando la vista FiltrosProductListView)
    path(
        'producto/reporte/', 
        views.FiltrosProductListView.as_view(),
        name='producto-filtros',  # Nombre de la ruta
    ),
]
