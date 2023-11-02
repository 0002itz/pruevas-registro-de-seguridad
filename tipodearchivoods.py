import pandas as pd
import pyexcel as pe

# Ruta al archivo .ods
archivo_ods = 'datos.ods'

# Leer el archivo .ods usando pyexcel-ods 
datos = pe.get_array(file_name=archivo_ods)

# Convertir los datos a un DataFrame de pandas
columnas = datos[0]
filas = datos[1:]
df = pd.DataFrame(filas, columns=columnas)

# Obtener las URLs de las columnas 8 y 11 en la fila 2
url_columna_8 = df.at[1, 'Columna8']  # Reemplaza 'Columna8' con el nombre real de tu columna 8
url_columna_11 = df.at[1, 'Columna11']  # Reemplaza 'Columna11' con el nombre real de tu columna 11

# Verificar y trabajar con las URLs si son válidas
if isinstance(url_columna_8, str) and url_columna_8.startswith(('http://', 'https://')) and url_columna_8.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
    print(f"URL de imagen en columna 8 (fila 2): {url_columna_8}")
else:
    print("No se encontró una URL válida en la columna 8 (fila 2).")

if isinstance(url_columna_11, str) and url_columna_11.startswith(('http://', 'https://')) and url_columna_11.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
    print(f"URL de imagen en columna 11 (fila 2): {url_columna_11}")
else:
    print("No se encontró una URL válida en la columna 11 (fila 2).")
