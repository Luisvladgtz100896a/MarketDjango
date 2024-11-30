from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import View
#
from .models import User

# Función que verifica si la ocupación del usuario permite acceder a una vista específica
def check_ocupation_user(ocupation, user_ocupation):
    # Si el rol de ocupación es 'ADMINISTRADOR' o el rol del usuario coincide con la ocupación proporcionada, permite el acceso
    if (ocupation == User.ADMINISTRADOR or ocupation == user_ocupation):
        return True
    else:
        return False


# Mixin para gestionar permisos de usuarios con rol 'Almacen'
class AlmacenPermisoMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users_app:user-login')  # Redirige al login si no está autenticado
    
    #LoginRequiredMixin LoginRequiredMixin obliga a usuario a estar autenticado antes de acceder a la vista, sino l oesta se redirige al onicio de seson.

    def dispatch(self, request, *args, **kwargs):
        # Verifica si el usuario está autenticado, si no lo está, se redirige al login. esa es la funcion del dispatch.
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        # Verifica si el rol del usuario es 'Almacen'. Si no, redirige al login.
        if not check_ocupation_user(request.user.ocupation, User.ALMACEN):
            return HttpResponseRedirect(
                reverse('users_app:user-login')
            )

        # Si tiene acceso, procede con la vista
        return super().dispatch(request, *args, **kwargs)


# Mixin para gestionar permisos de usuarios con rol ventas
class VentasPermisoMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users_app:user-login')  # Redirige al login si no está autenticado

    def dispatch(self, request, *args, **kwargs):
        # Verifica si el usuario está autenticado, si no lo está, se redirige al login
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        # Verifica si el rol del usuario es ventas. Si no, redirige al login.
        if not check_ocupation_user(request.user.ocupation, User.VENTAS):
            return HttpResponseRedirect(
                reverse('users_app:user-login')
            )

        # Si tiene acceso, procede con la vista
        return super().dispatch(request, *args, **kwargs)


# Mixin para gestionar permisos de usuarios con rol admin
class AdminPermisoMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users_app:user-login')  # Redirige al login si no está autenticado

    def dispatch(self, request, *args, **kwargs):
        # Verifica si el usuario está autenticado, si no lo está, se redirige al login
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        # Verifica si el rol del usuario es 'Administrador'. Si no, redirige al login.
        if not check_ocupation_user(request.user.ocupation, User.ADMINISTRADOR):
            return HttpResponseRedirect(
                reverse('users_app:user-login')
            )

        # Si tiene acceso, procede con la vista
        return super().dispatch(request, *args, **kwargs)
