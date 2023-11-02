import urllib
import ezodf
# Ruta al archivo .ods
archivo_ods = 'Registro_de_seguridad.ods'

# Función para descargar imágenes desde una URL
def descargar_imagen(url, nombre_archivo):
    urllib.request.urlretrieve(url, nombre_archivo)
    print(f"Imagen descargada desde {url} y guardada como {nombre_archivo}")

# Abrir el archivo .ods
doc = ezodf.opendoc(archivo_ods)

# Iterar a través de las hojas del archivo .ods
for hoja in doc.sheets:
    # Iterar a través de las celdas de la hoja
    for fila in hoja.rows():
        for celda in fila:
            # Verificar si la celda contiene una imagen (url que termina en .jpg, .png, etc.)
            if isinstance(celda.value, str) and celda.value.startswith(('http://', 'https://')) and celda.value.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                # Extraer el nombre del archivo de la URL
                nombre_archivo = celda.val.split('/')[-1]
                # Descargar la imagen
                descargar_imagen(celda.val, nombre_archivo)
