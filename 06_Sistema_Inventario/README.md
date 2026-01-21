# 📦 Dashboard de Gestión de Inventarios Inteligente

> Una aplicación web interactiva para el control de stock, visualización de datos y cálculo de activos en tiempo real.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey)

## 📖 Descripción del Proyecto

Este proyecto es una solución integral para la gestión de inventarios empresariales. A diferencia de las hojas de cálculo tradicionales, este sistema utiliza una base de datos relacional (**SQL**) conectada a una interfaz web moderna (**Streamlit**), permitiendo una integridad de datos superior y visualización instantánea.

El sistema permite registrar productos, monitorear niveles de stock bajos y visualizar el valor total de los activos mediante dashboards dinámicos.

## 🚀 Características Principales

* **📊 Dashboard de KPIs:** Cálculo automático en tiempo real de:
    * Total de productos en catálogo.
    * Valor monetario total del inventario.
    * Alertas de productos agotados (Stock 0).
* **💾 Base de Datos Persistente:** Uso de SQLite para almacenamiento seguro y estructurado.
* **⚡ Generación de Datos Sintéticos:** Algoritmo integrado para poblar la base de datos con información de prueba realista (ideal para demos).
* **➕ Gestión de Productos (CRUD):** Formulario lateral para ingresar nuevos productos directamente desde la interfaz de usuario sin tocar código.
* **📈 Visualización de Datos:** Gráficas de barras interactivas para analizar la distribución del stock.
* **🔍 Filtros y Ordenamiento:** Tabla de datos interactiva basada en Pandas.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python
* **Frontend:** Streamlit (para la interfaz web)
* **Backend/Data:** SQLite3 & Pandas
* **Entorno:** VS Code

## 💻 Instalación y Uso

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

1.  **Clonar el repositorio:**
    ```bash
    git clone [TU_LINK_DE_GITHUB_AQUI]
    ```

2.  **Instalar las dependencias:**
    Asegúrate de tener Python instalado y ejecuta:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Ejecutar la aplicación:**
    ```bash
    streamlit run app.py
    ```

4.  **¡Listo!** La aplicación se abrirá automáticamente en tu navegador web. La base de datos se creará sola la primera vez que inicies el programa.

---
**Desarrollado por Brian josue Pardo Saldaña**
*Ingeniero en Formación & Analista de Datos*