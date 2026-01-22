import sqlite3
import pandas as pd
import numpy as np
import os
import sys

# Forzar salida en UTF-8 para evitar errores de caracteres
sys.stdout.reconfigure(encoding='utf-8')

# Crear la carpeta data si no existe
if not os.path.exists('data'):
    os.makedirs('data')

# Conexión a la DB
conn = sqlite3.connect('data/ecommerce_master.db')

n_rows = 50000

data = {
    'id_venta': range(1, n_rows + 1),
    'fecha': pd.date_range(start='2024-01-01', periods=n_rows, freq='10min'),
    'producto': np.random.choice(['Smartphone', 'Laptop', 'Tablet', 'Smartwatch', 'Headphones'], n_rows),
    'cliente_id': np.random.randint(100, 5000, n_rows),
    'costo_unitario': np.random.uniform(50, 800, n_rows),
    'cantidad': np.random.randint(1, 10, n_rows),
    'metodo_pago': np.random.choice(['Credit Card', 'PayPal', 'Crypto', 'Transfer'], n_rows),
    'pais': np.random.choice(['Mexico', 'USA', 'Estonia', 'Germany', 'UK', 'Canada'], n_rows),
    'satisfaccion': np.random.randint(1, 6, n_rows)
}

df = pd.DataFrame(data)

df['precio_venta'] = df['costo_unitario'] * 1.3
df['ingreso_total'] = df['precio_venta'] * df['cantidad']
df['utilidad'] = df['ingreso_total'] - (df['costo_unitario'] * df['cantidad'])

# Guardar en SQL
df.to_sql('ventas', conn, if_exists='replace', index=False)

print("Exito: Base de datos creada en data/ecommerce_master.db")
conn.close()