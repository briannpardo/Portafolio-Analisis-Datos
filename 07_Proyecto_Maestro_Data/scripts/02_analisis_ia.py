import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

# --- CORRECCIÓN DE RUTA ---
# Subimos un nivel para salir de 'scripts' y entramos a 'data'
db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'ecommerce_master.db')

try:
    conn = sqlite3.connect(db_path)
    # 2. Cargar los datos
    df = pd.read_sql_query("SELECT * FROM ventas", conn)

    # 3. Inteligencia Artificial (Tendencia)
    X = np.array(df['id_venta']).reshape(-1, 1) 
    y = df['utilidad']
    modelo = LinearRegression()
    modelo.fit(X, y)
    df['tendencia_utilidad'] = modelo.predict(X)

    # 4. Guardar resultados
    df.to_sql('analisis_ia', conn, if_exists='replace', index=False)
    print("Exito: IA ejecutada correctamente.")
    conn.close()
except Exception as e:
    print(f"Error técnico: {e}")