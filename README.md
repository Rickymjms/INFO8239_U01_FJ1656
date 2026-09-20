# INF-8239: Ciencia de Datos II - Unidad 01
**Código:** U01.LAB00  
**Entorno de desarrollo reproducible**

## 1. Sistema Operativo y Herramientas
- **Sistema Operativo:** Windows 11 (64 bits)
- **Python:** 3.13
- **Control de versiones:** Git

## 2. Comandos para replicar y activar el entorno
```powershell
# Crear y activar entorno virtual
python -m venv .venv
.venv\Scripts\Activate.ps1

# Actualizar dependencias
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Ejecutar pruebas unitarias
$env:PYTHONPATH="src"
python -m pytest -q