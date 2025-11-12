# Script para iniciar el proyecto Gym Project en Windows (PowerShell)

Write-Host "========================================"
Write-Host "     GYM PROJECT - INICIO RAPIDO" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar si Python está instalado
try {
    python --version | Out-Null
} catch {
    Write-Host "ERROR: Python no está instalado o no está en PATH" -ForegroundColor Red
    Write-Host "Descarga Python desde: https://www.python.org" -ForegroundColor Yellow
    Read-Host "Presiona Enter para salir"
    exit 1
}

Write-Host "[1/5] Verificando entorno virtual..." -ForegroundColor Yellow
if (-not (Test-Path ".venv")) {
    Write-Host "[!] Creando entorno virtual..."
    python -m venv .venv
    Write-Host "[OK] Entorno virtual creado" -ForegroundColor Green
} else {
    Write-Host "[OK] Entorno virtual ya existe" -ForegroundColor Green
}

Write-Host ""
Write-Host "[2/5] Activando entorno virtual..." -ForegroundColor Yellow
& .\.venv\Scripts\Activate.ps1
Write-Host "[OK] Entorno virtual activado" -ForegroundColor Green

Write-Host ""
Write-Host "[3/5] Instalando/Actualizando dependencias..." -ForegroundColor Yellow
pip install -q -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: No se pudieron instalar las dependencias" -ForegroundColor Red
    Read-Host "Presiona Enter para salir"
    exit 1
}
Write-Host "[OK] Dependencias instaladas" -ForegroundColor Green

Write-Host ""
Write-Host "[4/5] Aplicando migraciones..." -ForegroundColor Yellow
python manage.py migrate --noinput
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: No se pudieron aplicar las migraciones" -ForegroundColor Red
    Read-Host "Presiona Enter para salir"
    exit 1
}
Write-Host "[OK] Migraciones aplicadas" -ForegroundColor Green

Write-Host ""
Write-Host "[5/5] Iniciando servidor Django..." -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Servidor ejecutándose en:" -ForegroundColor Cyan
Write-Host "  http://127.0.0.1:8000/" -ForegroundColor Green
Write-Host "" -ForegroundColor Cyan
Write-Host "  Presiona CTRL+C para detener" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

python manage.py runserver
