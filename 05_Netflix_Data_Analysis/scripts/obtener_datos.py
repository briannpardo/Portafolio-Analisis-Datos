import pandas as pd
import requests
import io
import os

# --- CONFIGURACIÓN ---
# 1. La URL donde está el archivo "raw" (crudo) en internet.
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2021/2021-04-20/netflix_titles.csv"
# 2. Definimos dónde queremos guardar el archivo.
nombre_archivo = 'netflix_titles.csv'
ruta_relativa = os.path.join('..', 'data', nombre_archivo)

print("⏳ Iniciando descarga de datos...")

try:
    # 3. Hacemos la petición a internet
    response = requests.get(url)
    
    # 4. Verificamos si la petición fue exitosa (Código 200 = OK)
    if response.status_code == 200:
        
        # 5. Convertimos el contenido de internet (texto) en un DataFrame de Pandas
        contenido_texto = response.content.decode('utf-8')
        df = pd.read_csv(io.StringIO(contenido_texto))
        
        # 6. Guardamos el archivo en la ruta que definimos arriba (carpeta data)
        df.to_csv(ruta_relativa, index=False)
        
        print(f"✅ ¡Éxito! Se descargaron {df.shape[0]} filas y {df.shape[1]} columnas.")
        print(f"📁 Archivo guardado en: {ruta_relativa}")
        
    else:
        print(f"❌ Error al conectar. Código: {response.status_code}")

except Exception as e:
    print(f"❌ Ocurrió un error inesperado: {e}")