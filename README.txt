¿Qué incluye AbstractUser?
AbstractUser es una clase base de Django que ya viene con los campos y funcionalidades típicas de un sistema de autenticación. Hereda de AbstractBaseUser y PermissionsMixin, y ya incluye:
🧾 Campos incorporados
|  |  |  | 
| username | CharField | Nombre de usuario único | 
| first_name | CharField | Nombre | 
| last_name | CharField | Apellido | 
| email | EmailField | correo electronico | 
| password | CharField | contraseña | 
| is_staff | BooleanField | acceso a admin | 
| is_active | BooleanField | si la cuenta está activa | 
| is_superuser | BooleanField | permisos totales | 
| last_login | DateTimeField | último acceso | 
| date_joined | DateTimeField | Fecah registro | 

MODULO ADMINISTRADOR
username admin
password admin




