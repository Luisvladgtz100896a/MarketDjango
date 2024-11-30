from django import forms  # Importa el módulo forms de Django para crear formularios.
from django.contrib.auth import authenticate  # Importa la función authenticate para validar usuarios.
from .models import User  # Importa el modelo de usuario personalizado definido en la aplicación actual.

# Formulario para registrar un nuevo usuario
class UserRegisterForm(forms.ModelForm):
    # Campo para la contraseña (primera entrada de contraseña).
    password1 = forms.CharField(
        label='Contraseña',  # Etiqueta del campo.
        required=True,  # Hace que este campo sea obligatorio.
        widget=forms.PasswordInput(  # Usa un widget de entrada de tipo contraseña.
            attrs={
                'placeholder': 'Contraseña',  # Texto de marcador de posición.
                'class': 'input-group-field',  # Clase CSS para estilizar el campo.
            }
        )
    )
    # Campo para repetir la contraseña (segunda entrada de contraseña).
    password2 = forms.CharField(
        label='Contraseña',  # Etiqueta del campo.
        required=True,  # Hace que este campo sea obligatorio.
        widget=forms.PasswordInput(  # Usa un widget de entrada de tipo contraseña.
            attrs={
                'placeholder': 'Repetir Contraseña',  # Texto de marcador de posición.
                'class': 'input-group-field',  # Clase CSS para estilizar el campo.
            }
        )
    )

    class Meta:
        """Define los metadatos del formulario, asociándolo con el modelo User."""
        model = User  # Asocia el formulario al modelo personalizado User.
        fields = (
            'email',  # Campo para el correo electrónico.
            'full_name',  # Campo para el nombre completo.
            'ocupation',  # Campo para la ocupación.
            'genero',  # Campo para el género.
            'date_birth',  # Campo para la fecha de nacimiento.
        )
        widgets = {
            'email': forms.EmailInput(  # Usa un widget para entradas de tipo correo electrónico.
                attrs={
                    'placeholder': 'Correo Electronico ...',  # Texto de marcador de posición.
                    'class': 'input-group-field',  # Clase CSS para estilizar el campo.
                }
            ),
            'full_name': forms.TextInput(  # Usa un widget para entradas de texto.
                attrs={
                    'placeholder': 'Nombres ...',  # Texto de marcador de posición.
                    'class': 'input-group-field',  # Clase CSS para estilizar el campo.
                }
            ),
            'ocupation': forms.Select(  # Usa un widget de selección para ocupación.
                attrs={
                    'placeholder': 'Ocupacion ...',  # Texto de marcador de posición.
                    'class': 'input-group-field',  # Clase CSS para estilizar el campo.
                }
            ),
            'date_birth': forms.DateInput(  # Usa un widget para entradas de tipo fecha.
                format='%Y-%m-%d',  # Especifica el formato de la fecha.
                attrs={
                    'type': 'date',  # Especifica el tipo de entrada HTML como fecha.
                    'class': 'input-group-field',  # Clase CSS para estilizar el campo.
                },
            ),
        }

    # Método para validar que las contraseñas coincidan
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:  # Verifica si las contraseñas no coinciden.
            self.add_error('password2', 'Las contraseñas no son iguales')  # Agrega un error al campo password2.


# Formulario para el inicio de sesión de los usuarios
class LoginForm(forms.Form):
    # Campo para el correo electrónico del usuario.
    email = forms.CharField(
        label='E-mail',  # Etiqueta del campo.
        required=True,  # Hace que este campo sea obligatorio.
        widget=forms.TextInput(  # Usa un widget de entrada de texto.
            attrs={
                'class': 'input-group-field',  # Clase CSS para estilizar el campo.
                'placeholder': 'Correo Electronico',  # Texto de marcador de posición.
            }
        )
    )
    # Campo para la contraseña del usuario.
    password = forms.CharField(
        label='Contraseña',  # Etiqueta del campo.
        required=True,  # Hace que este campo sea obligatorio.
        widget=forms.PasswordInput(  # Usa un widget de entrada de tipo contraseña.
            attrs={
                'class': 'input-group-field',  # Clase CSS para estilizar el campo.
                'placeholder': 'contraseña'  # Texto de marcador de posición.
            }
        )
    )

    # Método para validar que el usuario y contraseña sean correctos
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()  # Llama al método clean del formulario base.
        email = self.cleaned_data['email']  # Obtiene el correo electrónico del formulario.
        password = self.cleaned_data['password']  # Obtiene la contraseña del formulario.

        if not authenticate(email=email, password=password):  # Intenta autenticar al usuario.
            raise forms.ValidationError('Los datos de usuario no son correctos')  # Lanza un error si los datos son incorrectos.

        return self.cleaned_data  # Devuelve los datos validados.


# Formulario para actualizar los datos del usuario
class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User  # Asocia el formulario al modelo personalizado User.
        fields = (
            'email',  # Campo para el correo electrónico.
            'full_name',  # Campo para el nombre completo.
            'ocupation',  # Campo para la ocupación.
            'genero',  # Campo para el género.
            'date_birth',  # Campo para la fecha de nacimiento.
            'is_active',  # Campo para el estado activo del usuario.
        )
        widgets = {
            'email': forms.EmailInput(  # Usa un widget para entradas de tipo correo electrónico.
                attrs={
                    'placeholder': 'Correo Electronico ...',  # Texto de marcador de posición.
                    'class': 'input-group-field',  # Clase CSS para estilizar el campo.
                }
            ),
            'full_name': forms.TextInput(  # Usa un widget para entradas de texto.
                attrs={
                    'placeholder': 'Nombres ...',  # Texto de marcador de posición.
                    'class': 'input-group-field',  # Clase CSS para estilizar el campo.
                }
            ),
            'ocupation': forms.Select(  # Usa un widget de selección para ocupación.
                attrs={
                    'placeholder': 'Ocupacion ...',  # Texto de marcador de posición.
                    'class': 'input-group-field',  # Clase CSS para estilizar el campo.
                }
            ),
            'date_birth': forms.DateInput(  # Usa un widget para entradas de tipo fecha.
                format='%Y-%m-%d',  # Especifica el formato de la fecha.
                attrs={
                    'type': 'date',  # Especifica el tipo de entrada HTML como fecha.
                    'class': 'input-group-field',  # Clase CSS para estilizar el campo.
                },
            ),
            'is_active': forms.CheckboxInput(  # Usa un widget para un campo de selección tipo checkbox.
                attrs={},  # No requiere atributos adicionales.
            ),
        }


# Formulario para actualizar la contraseña del usuario
class UpdatePasswordForm(forms.Form):
    # Campo para la contraseña actual.
    password1 = forms.CharField(
        label='Contraseña',  # Etiqueta del campo.
        required=True,  # Hace que este campo sea obligatorio.
        widget=forms.PasswordInput(  # Usa un widget de entrada de tipo contraseña.
            attrs={
                'placeholder': 'Contraseña Actual'  # Texto de marcador de posición.
            }
        )
    )
    # Campo para la nueva contraseña.
    password2 = forms.CharField(
        label='Contraseña',  # Etiqueta del campo.
        required=True,  # Hace que este campo sea obligatorio.
        widget=forms.PasswordInput(  # Usa un widget de entrada de tipo contraseña.
            attrs={
                'placeholder': 'Nueva Contraseña'  # Texto de marcador de posición.
            }
        )
    )
