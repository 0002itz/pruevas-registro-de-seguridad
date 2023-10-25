import pandas as pd
import requests
from io import BytesIO
from PIL import Image

# Imagina que nuestro cuento comienza abriendo un misterioso documento llamado "datos.csv"
print("Había una vez un misterioso documento llamado 'datos.csv'...")

# Abrimos el documento .csv usando pandas
try:
    df = pd.read_csv('datos.csv')
    print("El documento se abrió mágicamente.")
except FileNotFoundError:
    print("Oh no! El documento no se encontró. El cuento termina tristemente.")
except pd.errors.EmptyDataError:
    print("¡El documento está vacío! Parece que la magia no está funcionando aquí.")
else:
    # Ahora, exploramos el contenido de este mágico documento
    print("Dentro del documento, encontramos columnas mágicas: ", df.columns.tolist())

    # Imaginemos que cada columna contiene el enlace a una imagen
    for columna in df.columns:
        print(f"Exploramos la columna mágica '{columna}'...")
        try:
            # Descargamos y mostramos las imágenes mágicas
            for enlace in df[columna]:
                response = requests.get(enlace)
                if response.status_code == 200:
                    imagen = Image.open(BytesIO(response.content))
                    imagen.show()
                    print("¡Hemos descargado y mostrado una imagen mágica!")
                else:
                    print(f"¡Oh no! No pudimos descargar la imagen del enlace: {enlace}")
        except KeyError:
            print(f"¡Oops! La columna '{columna}' no fue encontrada en este documento mágico.")

    print("Fin del cuento. ¡Espero que hayas disfrutado el viaje mágico a través del documento .csv!")