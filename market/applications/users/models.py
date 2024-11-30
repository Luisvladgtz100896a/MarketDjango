from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager

# Modelo de Usuario personalizado que extiende de AbstractBaseUser y PermissionsMixin
class User(AbstractBaseUser, PermissionsMixin):
    # Definición de tipos de usuarios (roles)
    ADMINISTRADOR = '0'
    ALMACEN = '1'
    VENTAS = '2'

    # Definición de géneros
    VARON = 'M'
    MUJER = 'F'
    OTRO = 'O'

    # Opciones de ocupación para los usuarios
    OCUPATION_CHOICES = [
        (ADMINISTRADOR, 'Administrador'),
        (ALMACEN, 'Almacen'),
        (VENTAS, 'Ventas'),
    ]

    # Opciones de género para los usuarios
    GENDER_CHOICES = [
        (VARON, 'Masculino'),
        (MUJER, 'Femenino'),
        (OTRO, 'Otros'),
    ]

    # Campos del modelo
    email = models.EmailField(unique=True)  # Correo electrónico único para cada usuario
    full_name = models.CharField('Nombres', max_length=100)  # Nombre completo del usuario
    ocupation = models.CharField(
        max_length=1, 
        choices=OCUPATION_CHOICES, 
        blank=True
    )  # Ocupación del usuario (Administrador, Almacen, Ventas)
    genero = models.CharField(
        max_length=1, 
        choices=GENDER_CHOICES, 
        blank=True
    )  # Género del usuario (Masculino, Femenino, Otro)
    date_birth = models.DateField(
        'Fecha de nacimiento', 
        blank=True,
        null=True
    )  # Fecha de nacimiento del usuario

    # Campos para el manejo de autenticación
    is_staff = models.BooleanField(default=False)  # Indica si el usuario tiene permisos de staff
    is_active = models.BooleanField(default=False)  # Indica si el usuario está activo en el sistema

    # Campo obligatorio para la autenticación
    USERNAME_FIELD = 'email'

    # Campos adicionales requeridos al crear un superusuario
    REQUIRED_FIELDS = ['full_name']

    # Utilización del manager personalizado para manejar usuarios
    objects = UserManager()

    # Métodos para obtener el nombre corto y completo del usuario
    def get_short_name(self):
        return self.email
    
    def get_full_name(self):
        return self.full_name
