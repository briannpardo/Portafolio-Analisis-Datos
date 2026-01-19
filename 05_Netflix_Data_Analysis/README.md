# 🎬 Análisis Exploratorio de Datos (EDA) - Netflix

Este proyecto realiza un análisis completo sobre el catálogo de Netflix. El objetivo es procesar datos crudos (descargados automáticamente) para limpiar la información y descubrir tendencias en la estrategia de contenido de la plataforma (Películas vs Series).

## 📂 Estructura del Proyecto

Este repositorio sigue una estructura de Ciencia de Datos profesional:

* **`data/`**: Carpeta contenedora del dataset `netflix_titles.csv` (se descarga vía script).
* **`scripts/`**: Contiene `obtener_datos.py`, el código para automatizar la descarga de datos desde la nube.
* **`notebooks/`**: Contiene `01_limpieza_y_analisis.ipynb`, donde se realiza la limpieza de datos, tratamiento de nulos y visualización.
* **`reports/`**: Contiene las gráficas generadas en PNG y el **Reporte Ejecutivo de Resultados**.

## 🚀 Requisitos e Instalación

El proyecto utiliza Python 3.12 y las siguientes librerías de análisis:
```bash
pip install pandas matplotlib seaborn requests
```

# ⚙️ Instrucciones de Ejecución
Sigue estos pasos para reproducir el análisis:

1. Ingestión de Datos: Ejecuta el script para descargar los datos más recientes a tu disco local:
```bash
cd scripts
python obtener_datos.py
```
2. Análisis y Visualización: Abre el archivo dentro de la carpeta notebooks/ usando Jupyter para ver el paso a paso del análisis exploratorio.

📊 Resultados del Análisis
El estudio reveló un cambio de estrategia en Netflix a partir de 2019, priorizando la retención mediante series.

👉 [Leer el Reporte Ejecutivo con Gráficas aquí](reports/Reporte_Resultados_Netflix.md)

Autor: Brian Pardo | Portafolio de Data Analysis