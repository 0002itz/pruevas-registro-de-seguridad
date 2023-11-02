import pandas as pd
from pyexcel_ods import get_data

# Ruta al archivo .ods
archivo_ods = 'C:/Users/rodri/OneDrive/Documentos/Playgraund/pruevas registro de seguridad/Registro_de_seguridad.ods'

# Leer el archivo .ods
datos = get_data(archivo_ods)

# Obtener las URLs de las columnas 8 y 11 en la fila 2
url_columna_8 = datos['Hoja 1'][1][8]  # Reemplaza 'Sheet1' con el nombre real de tu hoja y ajusta los índices según tu archivo
url_columna_11 = datos['Hoja 1'][1][11]  # Reemplaza 'Sheet1' con el nombre real de tu hoja y ajusta los índices según tu archivo

# Verificar y trabajar con las URLs si son válidas
if isinstance(url_columna_8, str) and url_columna_8.startswith(('http://', 'https://')) and url_columna_8.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
    print(f"URL de imagen en columna 8 (fila 2): {url_columna_8}")
else:
    print("No se encontró una URL válida en la columna 8 (fila 2).")

if isinstance(url_columna_11, str) and url_columna_11.startswith(('http://', 'https://')) and url_columna_11.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
    print(f"URL de imagen en columna 11 (fila 2): {url_columna_11}")
else:
    print("No se encontró una URL válida en la columna 11 (fila 2).")