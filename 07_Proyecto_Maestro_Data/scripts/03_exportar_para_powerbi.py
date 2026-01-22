import sqlite3
import pandas as pd
import os

# Ruta a la base de datos
db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'ecommerce_master.db')
conn = sqlite3.connect(db_path)

# Leemos la tabla que ya tiene la Inteligencia Artificial
df = pd.read_sql_query("SELECT * FROM analisis_ia", conn)

# Lo guardamos como CSV (que Power BI lee instantáneamente)
csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'datos_finales.csv')
df.to_csv(csv_path, index=False, encoding='utf-8-sig')

print("Exito: Archivo 'datos_finales.csv' creado para Power BI.")
conn.close()