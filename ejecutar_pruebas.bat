@echo off
REM Script para ejecutar las pruebas del proyecto Gym Project

echo ========================================
echo     GYM PROJECT - EJECUTAR PRUEBAS
echo ========================================
echo.

REM Activar entorno virtual
call .venv\Scripts\activate.bat

echo.
echo Selecciona qué pruebas ejecutar:
echo.
echo 1. Todas las pruebas (20 pruebas)
echo 2. Pruebas de usuarios (15 pruebas)
echo 3. Pruebas de web (5 pruebas)
echo 4. Prueba específica
echo 5. Pruebas con cobertura
echo 6. Salir
echo.

set /p choice="Opción (1-6): "

if "%choice%"=="1" (
    echo.
    echo Ejecutando todas las pruebas...
    echo.
    python manage.py test --verbosity=2
) else if "%choice%"=="2" (
    echo.
    echo Ejecutando pruebas de usuarios...
    echo.
    python manage.py test usuarios.tests --verbosity=2
) else if "%choice%"=="3" (
    echo.
    echo Ejecutando pruebas de web...
    echo.
    python manage.py test web.tests --verbosity=2
) else if "%choice%"=="4" (
    echo.
    set /p test="Nombre de la prueba (ej: usuarios.tests.UsuarioModelTests.test_crear_usuario_cliente): "
    echo.
    python manage.py test %test%
) else if "%choice%"=="5" (
    echo.
    pip install coverage >nul 2>&1
    echo Ejecutando pruebas con cobertura...
    echo.
    coverage run --source='.' manage.py test
    echo.
    echo Reporte de cobertura:
    echo.
    coverage report
    echo.
    echo Generando reporte HTML en htmlcov/index.html...
    coverage html
    echo [OK] Reporte HTML generado
) else if "%choice%"=="6" (
    exit /b 0
) else (
    echo Opción no válida
    pause
    exit /b 1
)

echo.
echo ========================================
echo     PRUEBAS COMPLETADAS
echo ========================================

pause
