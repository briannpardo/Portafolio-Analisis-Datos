import streamlit as st
import pandas as pd
import sqlite3
import os
import random

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Sistema de Inventario", layout="wide")

# --- CONEXIÓN A LA BASE DE DATOS ---
ruta_db = os.path.join("data", "inventario.db")

def conectar_db():
    return sqlite3.connect(ruta_db)

# --- FUNCIÓN PARA CREAR TABLA Y DATOS ---
def inicializar_datos():
    # Nos aseguramos que la carpeta 'data' exista
    if not os.path.exists("data"):
        os.makedirs("data")
        
    conn = conectar_db()
    cursor = conn.cursor()
    
    # 1. Crear tabla
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            stock INTEGER,
            precio REAL
        )
    ''')
    conn.commit()

    # 2. Verificar si está vacía
    cursor.execute("SELECT COUNT(*) FROM productos")
    filas = cursor.fetchone()[0]
    
    if filas == 0:
        marcas = ["HP", "Dell", "Logitech", "Samsung", "Sony", "Apple", "Asus", "Lenovo"]
        items = ["Monitor", "Teclado", "Mouse", "Laptop", "Cable HDMI", "Audífonos", "Cámara Web", "Disco Duro"]
        
        productos_masivos = []
        for _ in range(50):
            nombre = f"{random.choice(marcas)} {random.choice(items)}"
            stock = random.randint(0, 100)
            precio = round(random.uniform(100, 25000), 2)
            productos_masivos.append((nombre, stock, precio))
        
        cursor.executemany("INSERT INTO productos (nombre, stock, precio) VALUES (?, ?, ?)", productos_masivos)
        conn.commit()
    
    conn.close()

# --- FUNCIÓN PARA CARGAR LOS DATOS ---
def cargar_datos():
    conn = conectar_db()
    df = pd.read_sql("SELECT * FROM productos", conn)
    conn.close()
    return df

# --- EJECUCIÓN PRINCIPAL ---
st.title("📦 Control de Inventario Inteligente")

# 1. Primero preparamos la base de datos
inicializar_datos()

# 2. Luego cargamos los datos
df_inventario = cargar_datos()

# 3. Mostramos las métricas (KPIs)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total de Productos", len(df_inventario))
with col2:
    total_valor = (df_inventario['stock'] * df_inventario['precio']).sum()
    st.metric("Valor del Inventario", f"${total_valor:,.2f}")
with col3:
    agotados = len(df_inventario[df_inventario['stock'] == 0])
    st.metric("Productos Agotados", agotados, delta_color="inverse")

st.markdown("---")

# 4. Mostramos la tabla interactiva
st.subheader("📋 Detalle de Existencias")
st.dataframe(df_inventario, use_container_width=True)

# 5. Gráfico de barras (Bonus para que se vea Pro)
st.subheader("📊 Niveles de Stock por Producto")
st.bar_chart(df_inventario.set_index('nombre')['stock'])

# --- FORMULARIO PARA AGREGAR PRODUCTOS (En la barra lateral) ---
st.sidebar.header("➕ Agregar Nuevo Producto")

with st.sidebar.form("form_nuevo_producto"):
    nuevo_nombre = st.text_input("Nombre del Producto")
    nuevo_stock = st.number_input("Cantidad en Stock", min_value=0, step=1)
    nuevo_precio = st.number_input("Precio Unitario", min_value=0.0, step=10.0)
    
    boton_guardar = st.form_submit_button("Guardar Producto")

    if boton_guardar:
        if nuevo_nombre:
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO productos (nombre, stock, precio) VALUES (?, ?, ?)", 
                           (nuevo_nombre, nuevo_stock, nuevo_precio))
            conn.commit()
            conn.close()
            st.success(f"¡{nuevo_nombre} agregado con éxito!")
            st.rerun() # Esto recarga la página para que el nuevo producto aparezca en la tabla
        else:
            st.error("Por favor, escribe un nombre.")