from io import BytesIO
import os
from PIL import Image
import pandas as pd
import requests

# Ruta al archivo CSV
archivo_csv = 'C:/Users/rodri/OneDrive/Documentos/Playgraund/pruevas registro de seguridad/Registro de seguridad - Hoja 1.csv'

# Verificar si el archivo CSV existe
if os.path.exists(archivo_csv):
    # Leer el archivo CSV usando pandas
    df = pd.read_csv(archivo_csv)

    try:
        # Obtener las URLs de la octava y undécima columna de la fila 2
        octava_columna_url = df.iloc[1, 8]  # Octava columna, fila 2
        onceava_columna_url = df.iloc[1, 11]  # Onceava columna, fila 2

        # Descargar las imágenes desde las URLs especificadas
        response_octava = requests.get(octava_columna_url)
        response_onceava = requests.get(onceava_columna_url)

        if response_octava.status_code == 200:
            imagen_octava = Image.open(BytesIO(response_octava.content))
            imagen_octava.save('octava_columna.jpg')
            print(f"Imagen de la octava columna descargada desde {octava_columna_url}")

        if response_onceava.status_code == 200:
            imagen_onceava = Image.open(BytesIO(response_onceava.content))
            imagen_onceava.save('onceava_columna.jpg')
            print(f"Imagen de la onceava columna descargada desde {onceava_columna_url}")

    except Exception as e:
        print(f"Error al descargar las imágenes: {str(e)}")

else:
    print(f"El archivo {archivo_csv} no existe.")