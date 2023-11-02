from io import BytesIO
from PIL import Image
import os
import pandas as pd
import requests

# Ruta al archivo CSV
archivo_csv = "C:/Users/rodri/OneDrive/Documentos/Playgraund/pruevas registro de seguridad/registro_de_entrada.csv"

# Verificar si el archivo CSV existe
if os.path.exists(archivo_csv):
    # Leer el archivo CSV usando pandas
    df = pd.read_csv(archivo_csv)

    # Iterar a través de las columnas del DataFrame
    for columna in df.columns:
        # Iterar a través de las filas de la columna actual
        for enlace in df[columna]:
            try:
                # Descargar la imagen desde la URL
                response = requests.get(enlace)
                if response.status_code == 200:
                    # Abrir la imagen utilizando Pillow (PIL)
                    imagen = Image.open(BytesIO(response.content))

                    # Mostrar o guardar la imagen (aquí está el lugar para personalizar)
                    imagen.show()  # Esto mostrará la imagen
                    # imagen.save('nombre_de_archivo.jpg')  # Esto guardará la imagen

                    print(f"Imagen descargada desde {enlace}")
                else:
                    print(f"No se pudo descargar la imagen desde {enlace}")
            except Exception as e:
                print(f"Error al procesar la URL {enlace}: {str(e)}")
else:
    print(f"El archivo {archivo_csv} no existe.")