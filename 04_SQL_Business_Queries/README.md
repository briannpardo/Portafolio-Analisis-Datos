# 🗄️ SQL Business Queries - Gestión de Inventario

En este proyecto, dejé de usar archivos CSV para trabajar con una **Base de Datos Relacional (SQLite)**. Diseñé una estructura desde cero para gestionar el inventario de una tienda tecnológica.

## 🚀 Lo que aprendí y apliqué:
* **DDL (Data Definition Language):** Creación de tablas con tipos de datos específicos (INTEGER, TEXT, REAL) y llaves primarias.
* **DML (Data Manipulation Language):** Inserción de registros y actualización de datos.
* **Consultas de Negocio:**
    * Filtrado de productos con bajo stock (`WHERE`).
    * Identificación de productos premium mediante ordenamiento (`ORDER BY` y `LIMIT`).
    * Cálculo del valor total de activos en bodega usando funciones de agregación (`SUM`).

## 🛠️ Estructura del Proyecto:
* `/data`: Contiene la base de datos `tienda.db`.
* `/scripts`: Archivos `.sql` con los comandos de creación, carga y consulta.

## 📈 Impacto de Negocio
Este sistema permite a un gerente identificar en segundos qué productos necesitan reabastecimiento y cuál es el capital invertido en mercancía, facilitando la toma de decisiones financieras.