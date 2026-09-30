# INF-8239 · Ciencia de Datos II

Repositorio académico oficial para el desarrollo de prácticas, laboratorios y proyectos de la asignatura **Ciencia de Datos II (INF-8239)** de la Maestría en Ciencia de Datos e Inteligencia Artificial en la **Universidad Autónoma de Santo Domingo (UASD)**[cite: 8].

---

## 1. Información General y Autoría
- **Institución Educativa:** Universidad Autónoma de Santo Domingo (UASD)[cite: 8]
- **Asignatura:** Ciencia de Datos II (INF-8239)[cite: 8]
- **Docente / Autor del Contenido:** Edwin Ramón José Nolasco[cite: 8]
- **Estudiante / Autor del Repositorio:** Manuel De Jesus Mañana Santana[cite: 4]
- **Unidad de Trabajo:** Unidad 01 - Modelos avanzados, reducción dimensional y Green AI[cite: 5]

---

## 2. Sistema Operativo y Herramientas (Entorno Base)
- **Sistema Operativo:** Windows 11 (64 bits)
- **Python:** 3.13
- **Control de versiones:** Git
- **Editor:** Visual Studio Code

---

## 3. Estructura del Repositorio
El proyecto sigue una arquitectura modular, reproducible y orientada a buenas prácticas de ingeniería de Machine Learning y *Green AI*[cite: 5]:
- **`data/`**: Almacena los datasets públicos descargados de forma automatizada y reproducible (`data/raw/` protegido por contrato de datos)[cite: 4].
- **`notebooks/`**: Cuadernos interactivos organizados para la experimentación, validación y ejecución de laboratorios[cite: 4].
- **`src/`**: Módulos de código fuente reutilizables para la carga de datos, pipelines y transformaciones[cite: 4, 9].
- **`tests/`**: Pruebas unitarias automatizadas (`pytest`) para validar esquemas y contratos de datos[cite: 4, 9].
- **`reports/`**: Modelos entrenados serializados, figuras de evaluación y métricas de desempeño[cite: 4, 9].
- **`docs/`**: Documentación técnica, fichas de procedencia y diccionarios de variables[cite: 4].
- **`Practicas/`**: Carpeta designada para las actividades y entregables prácticos versionados y respaldados en GitHub[cite: 4].
- **`Unidades/`**: Carpeta auxiliar de estudio local excluida del control de versiones mediante `.gitignore`.

---

## 4. Unidades y Contenido de la Asignatura
1. **Unidad 01: Modelos avanzados, reducción dimensional y Green AI**[cite: 5]
   - *LAB00:* Preparación y validación del entorno profesional (Entorno reproducible)[cite: 5].
   - *LAB01 & LAB02:* Pipelines con SVM sin fuga de datos, búsqueda de hiperparámetros y auditoría de datasets públicos (Ejercicio 01)[cite: 1, 5].
   - *LAB03:* Ensambles (Random Forest, Boosting), reducción dimensional (PCA, t-SNE) y análisis de eficiencia bajo criterios de *Green AI* (Ejercicio 02)[cite: 5].
2. **Unidades Posteriores:** *(Espacio reservado para los siguientes módulos del plan de estudio)*

---

## 5. Comandos para Replicar y Activar el Entorno

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