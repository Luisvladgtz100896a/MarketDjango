from django.urls import path

from . import views

app_name = "users_app"  # Define el nombre del espacio de nombres para la aplicación

urlpatterns = [
    # Ruta para el login del usuario
    path(
        '', 
        views.LoginUser.as_view(),  # Vista que maneja el inicio de sesión
        name='user-login',  # Nombre de la URL para esta vista
    ),
    
    # Ruta para registrar un nuevo usuario
    path(
        'users/register/', 
        views.UserRegisterView.as_view(),  # Vista que maneja el registro de usuarios
        name='user-register',  # Nombre de la URL para esta vista
    ),
    
    # Ruta para cerrar sesión del usuario
    path(
        'users/logout/', 
        views.LogoutView.as_view(),  # Vista que maneja el cierre de sesión
        name='user-logout',  # Nombre de la URL para esta vista
    ),
    
    # Ruta para actualizar la contraseña del usuario
    path(
        'users/update-password/<pk>/', 
        views.UpdatePasswordView.as_view(),  # Vista que maneja la actualización de la contraseña
        name='user-update_password',  # Nombre de la URL para esta vista
    ),
    
    # Ruta para actualizar los datos de un usuario
    path(
        'users/update/<pk>/', 
        views.UserUpdateView.as_view(),  # Vista que maneja la actualización de los datos del usuario
        name='user-update',  # Nombre de la URL para esta vista
    ),
    
    # Ruta para eliminar un usuario
    path(
        'users/delete/<pk>/', 
        views.UserDeleteView.as_view(),  # Vista que maneja la eliminación de un usuario
        name='user-delete',  # Nombre de la URL para esta vista
    ),
    
    # Ruta para ver la lista de usuarios
    path(
        'users/lista/', 
        views.UserListView.as_view(),  # Vista que muestra la lista de usuarios
        name='user-lista',  # Nombre de la URL para esta vista
    ),
]
