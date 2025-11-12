@echo off
REM Script para iniciar el proyecto Gym Project en Windows

echo ========================================
echo     GYM PROJECT - INICIO RAPIDO
echo ========================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no está instalado o no está en PATH
    echo Descarga Python desde: https://www.python.org
    pause
    exit /b 1
)

echo [1/5] Verificando entorno virtual...
if not exist ".venv" (
    echo [!] Creando entorno virtual...
    python -m venv .venv
    echo [OK] Entorno virtual creado
) else (
    echo [OK] Entorno virtual ya existe
)

echo.
echo [2/5] Activando entorno virtual...
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: No se pudo activar el entorno virtual
    pause
    exit /b 1
)
echo [OK] Entorno virtual activado

echo.
echo [3/5] Instalando/Actualizando dependencias...
pip install -q -r requirements.txt
if errorlevel 1 (
    echo ERROR: No se pudieron instalar las dependencias
    pause
    exit /b 1
)
echo [OK] Dependencias instaladas

echo.
echo [4/5] Aplicando migraciones...
python manage.py migrate --noinput
if errorlevel 1 (
    echo ERROR: No se pudieron aplicar las migraciones
    pause
    exit /b 1
)
echo [OK] Migraciones aplicadas

echo.
echo [5/5] Iniciando servidor Django...
echo.
echo ========================================
echo  Servidor ejecutándose en:
echo  http://127.0.0.1:8000/
echo.
echo  Presiona CTRL+BREAK para detener
echo ========================================
echo.

python manage.py runserver

pause
