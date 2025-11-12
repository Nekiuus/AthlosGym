# Pruebas de Software - Gym Project

Se han creado y ejecutado 20 pruebas unitarias que validan la funcionalidad del sistema.

## Resultados

- ✅ 20/20 pruebas PASADAS
- Usuarios: 15 pruebas
- Web: 5 pruebas
- Tiempo total: ~11 segundos

## Ejecutar las Pruebas

```bash
# Todas las pruebas
python manage.py test --verbosity=2

# Solo usuarios (15 pruebas)
python manage.py test usuarios.tests --verbosity=2

# Solo web (5 pruebas)
python manage.py test web.tests --verbosity=2

# Una prueba específica
python manage.py test usuarios.tests.UsuarioModelTests.test_crear_usuario_cliente

# Con reporte de cobertura
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Genera htmlcov/index.html
```

## Pruebas del Modelo Usuario (5 pruebas)

- **test_crear_usuario_cliente**: Validar creación de usuario con rol cliente
- **test_usuario_tiene_atributos_correctos**: Verificar atributos (teléfono, dirección, rol)
- **test_usuario_rol_valido**: Validar que rol está entre las opciones válidas
- **test_usuario_autenticacion**: Verificar que la autenticación funciona
- **test_crear_usuario_admin**: Validar creación de usuario administrador

## Pruebas del Formulario de Registro (3 pruebas)

- **test_formulario_registro_valido**: Aceptar datos válidos
- **test_formulario_registro_contrasenas_diferentes**: Rechazar contraseñas que no coinciden
- **test_formulario_registro_usuario_duplicado**: Rechazar usuarios con username existente

## Pruebas de Vistas de Usuarios (7 pruebas)

- **test_pagina_registro_carga**: Página de registro carga correctamente
- **test_registro_usuario_exitoso**: Usuario se registra en la base de datos
- **test_login_usuario_exitoso**: Login funciona correctamente
- **test_login_usuario_invalido**: Login rechaza credenciales inválidas
- **test_logout_usuario**: Logout limpia la sesión
- **test_inicio_privado_sin_autenticacion**: Redirige a login sin autenticación
- **test_inicio_privado_con_autenticacion**: Página privada es accesible con login

## Pruebas de Vistas Web (2 pruebas)

- **test_inicio_publico_carga**: Página de inicio carga correctamente
- **test_navbar_existe**: El navbar se renderiza en la página

## Pruebas de Configuración (3 pruebas)

- **test_url_index**: URL de inicio funciona
- **test_url_admin_existe**: URL de admin funciona
- **test_template_navbar_exists**: Template del navbar existe

## Aspectos Validados

✅ Creación y autenticación de usuarios
✅ Validación de formularios
✅ Seguridad (contraseñas, duplicados)
✅ Autenticación y autorización
✅ Cargas de URLs y templates
✅ Redirecciones de seguridad

## Comandos Útiles

```bash
# Ver las migraciones
python manage.py showmigrations

# Crear nuevas migraciones
python manage.py makemigrations

# Ver SQL de migraciones
python manage.py sqlmigrate usuarios 0001

# Limpiar la base de datos
python manage.py flush

# Entrar a Django shell
python manage.py shell
```
