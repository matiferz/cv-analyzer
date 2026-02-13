# CV Analyzer (Python)

Sistema en Python para analizar currículums en formato PDF, extraer información relevante y compararla contra los requisitos de un puesto laboral.

Este proyecto forma parte de un portfolio profesional y simula el funcionamiento básico de un ATS (Applicant Tracking System) utilizado en procesos reales de selección de personal.

---

## Importante

- El proyecto no incluye ningún CV cargado por defecto.
- Para utilizar el sistema, el usuario debe proporcionar su propio archivo PDF al ejecutar el programa.
- Los requisitos del puesto se definen manualmente dentro del código para simular ofertas laborales reales y garantizar un análisis transparente y explicable.

---

## Funcionalidades

- Lectura de CVs en formato PDF
- Extracción automática de:
  - Email de contacto
  - Habilidades técnicas
- Clasificación de requisitos por categoría:
  - Lenguajes
  - Herramientas
  - Sistemas
- Comparación entre el perfil del CV y los requisitos del puesto
- Cálculo de porcentaje de coincidencia (matching)
- Resultados claros y explicables por consola

---

## ¿Cómo funciona?

1. El sistema recibe como parámetro la ruta a un archivo PDF.
2. Convierte el contenido del PDF a texto plano.
3. Analiza el texto buscando patrones (email) y palabras clave (habilidades).
4. Detecta requisitos del puesto agrupados por categoría.
5. Compara las habilidades detectadas contra los requisitos definidos.
6. Devuelve un resumen del análisis y el porcentaje de coincidencia.

El sistema prioriza precisión y transparencia, evitando falsos positivos.

---

## Tecnologías utilizadas

- Python 3
- PyPDF2 (lectura de PDFs)
- Expresiones regulares (`re`)
- Estructura modular (arquitectura por capas)

---

## Estructura del proyecto

```bash
cv_analyzer/
│
├── data/
│   └── cvs/
│
├── src/
│   ├── main.py
│   ├── reader.py
│   ├── extractor.py
│   ├── analyzer.py
│   └── matcher.py
│
├── .gitignore
└── README.md
```

---

## Cómo ejecutar el proyecto

1. Clonar el repositorio.
2. Instalar dependencias:

```bash
pip install PyPDF2
```

3. Colocar un CV en formato PDF dentro de `data/cvs/`.
4. Ejecutar el programa indicando la ruta del archivo:

```bash
python src/main.py data/cvs/tu_cv.pdf
```

---

## Ejemplo de salida

```bash
=== RESULTADO DEL ANALISIS ===
Email detectado: ejemplo@email.com

Habilidades detectadas: ['java', 'sql']
Match con el puesto: 33.33%
Coincidencias: ['sql']

--- REQUISITOS DETECTADOS ---
Lenguajes: ['java', 'sql']
Herramientas: []
Sistemas: []
```

---

## Posibles mejoras futuras

- Soporte para múltiples CVs y ranking automático
- Exportación de resultados a JSON o CSV
- Interfaz gráfica o API REST
- Ampliación de sinónimos y alias de habilidades
- Integración con bases de datos

---

## Autor

Proyecto desarrollado por Matías Fernández como parte de su portfolio de desarrollo en Python.

---

## Nota final

Este proyecto no utiliza inteligencia artificial ni machine learning a propósito, priorizando un diseño claro, explicable y extensible, alineado con sistemas reales de análisis de CVs.