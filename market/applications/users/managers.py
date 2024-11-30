from django.contrib.auth.models import UserManager

# Manager personalizado para el modelo de Usuario
class UserManager(UserManager):
    # Método para crear un usuario normal
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password) # encripta la clave antes de guardarla en la base de datos
        user.save(using=self._db)
        return user

    # Método para crear un superusuario
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)

    # Método para obtener todos los usuarios que no son superusuarios
    def usuarios_sistema(self):
        return self.filter(is_superuser=False).order_by('-last_login')

