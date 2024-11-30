from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from django.views.generic import (
    View,
    CreateView,
    ListView,
    UpdateView,
    DeleteView
)

from django.views.generic.edit import (
    FormView
)

from .forms import (
    UserRegisterForm, 
    LoginForm,
    UserUpdateForm,
    UpdatePasswordForm,
)
#
from .models import User
#

# Vista para registrar un nuevo usuario
class UserRegisterView(FormView):
    template_name = 'users/register.html'  # Plantilla que se renderiza
    form_class = UserRegisterForm  # Formulario para registrar un nuevo usuario
    success_url = reverse_lazy('users_app:user-lista')  # URL de redirección al éxito

    def form_valid(self, form):
        # Crea un nuevo usuario utilizando los datos del formulario
        User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            full_name=form.cleaned_data['full_name'],
            ocupation=form.cleaned_data['ocupation'],
            genero=form.cleaned_data['genero'],
            date_birth=form.cleaned_data['date_birth'],
        )
        # Aquí podría enviar un correo de confirmación al usuario
        # send_mail("Bienvenido", "Gracias por registrarte", "info@miapp.com", [form.cleaned_data['email']])
        
        # Después de registrar al usuario, se redirige al éxito
        return super(UserRegisterView, self).form_valid(form)


# Vista para iniciar sesión de un usuario
class LoginUser(FormView):
    template_name = 'users/login.html'  # Plantilla que se renderiza
    form_class = LoginForm  # Formulario para iniciar sesión
    success_url = reverse_lazy('home_app:index')  # URL de redirección al éxito (página principal)

    def form_valid(self, form):
        # Intenta autenticar al usuario con el correo y la contraseña del formulario
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        # Si el usuario es válido, se realiza el login
        login(self.request, user)
        
        # Después de iniciar sesión con éxito, redirige al éxito
        return super(LoginUser, self).form_valid(form)


# Vista para cerrar sesión de un usuario
class LogoutView(View):
    def get(self, request, *args, **kargs):
        # Cierra la sesión del usuario
        logout(request)
        
        # Redirige al usuario a la página de login
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )


# Vista para actualizar los datos de un usuario
class UserUpdateView(UpdateView):
    template_name = "users/update.html"  # Plantilla que se renderiza
    model = User  # El modelo de datos a actualizar
    form_class = UserUpdateForm  # Formulario para actualizar los datos del usuario
    success_url = reverse_lazy('users_app:user-lista')  # URL de redirección al éxito

# Vista para eliminar un usuario
class UserDeleteView(DeleteView):
    model = User  # El modelo de datos que se eliminará
    success_url = reverse_lazy('users_app:user-lista')  # URL de redirección al éxito (lista de usuarios)


# Vista para actualizar la contraseña de un usuario
class UpdatePasswordView(LoginRequiredMixin, FormView):
    # form_class = UpdatePasswordForm  # Formulario para actualizar la contraseña
    success_url = reverse_lazy('users_app:user-login')  # Redirige al login después de la actualización
    login_url = reverse_lazy('users_app:user-login')  # Redirige al login si no está autenticado

    def form_valid(self, form):
        # Obtiene el usuario actual
        usuario = self.request.user
        # Autentica al usuario con la contraseña actual
        user = authenticate(
            email=usuario.email,
            password=form.cleaned_data['password1']
        )

        if user:
            # Si la contraseña actual es correcta, establece la nueva contraseña
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()

        # Cierra la sesión del usuario después de cambiar la contraseña
        logout(self.request)
        
        # Redirige al usuario al éxito después de cambiar la contraseña
        return super(UpdatePasswordView, self).form_valid(form)


# Vista para mostrar una lista de usuarios
class UserListView(ListView):
    template_name = "users/lista.html"  # Plantilla que se renderiza
    context_object_name = 'usuarios'  # Nombre del contexto en la plantilla

    def get_queryset(self):
        # Obtiene los usuarios del sistema (probablemente un método personalizado de User)
        return User.objects.usuarios_sistema()
