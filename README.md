# Gym Project

Sistema de gestión para gimnasio desarrollado con Django 5.2.8. Incluye autenticación de usuarios, carrito de compras y catálogo de productos.

## Requisitos

- Python 3.13+
- pip

## Instalación Rápida

```bash
# Crear entorno virtual
python -m venv .venv

# Activar (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones
python manage.py migrate
```

## Iniciar el servidor

```bash
python manage.py runserver
```

Luego abre http://127.0.0.1:8000/ en tu navegador.

## Ejecutar las pruebas

```bash
# Todas las pruebas (20 pruebas)
python manage.py test --verbosity=2

# Solo usuarios (15 pruebas)
python manage.py test usuarios.tests --verbosity=2

# Solo web (5 pruebas)
python manage.py test web.tests --verbosity=2
```

## URLs principales

- `/` - Inicio público
- `/registro/` - Registrarse
- `/login/` - Login
- `/inicio/` - Página privada (requiere login)
- `/app/` - Panel del usuario
- `/app/producto/` - Productos
- `/app/carritocompras/` - Carrito
- `/admin/` - Panel de admin

## Crear superusuario

```bash
python manage.py createsuperuser
```

Luego entra a http://127.0.0.1:8000/admin/

## Cambiar a MySQL

Si quieres usar MySQL en lugar de SQLite:

1. Edita `gym_project/settings.py`
2. Descomenta la configuración de MySQL
3. Actualiza los datos de conexión
4. Corre `python manage.py migrate`

Ver PRUEBAS_SOFTWARE.md para más detalles sobre las pruebas.
