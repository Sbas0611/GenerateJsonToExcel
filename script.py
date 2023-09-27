import json
import pandas as pd
import glob
import concurrent.futures

# Define el directorio donde se encuentran tus archivos .xlsx
# Reemplaza con la ubicación de tus archivos .xlsx
directorio = 'data'

# Utiliza glob para buscar todos los archivos .xlsx en el directorio
archivos_xlsx = glob.glob(f'{directorio}/*.xlsx')

# Función para procesar un archivo .xlsx y convertirlo a JSON


def procesar_xlsx(archivo_xlsx):
    try:
        # Lee el archivo .xlsx en un DataFrame de pandas
        df = pd.read_excel(archivo_xlsx)

        # Convierte el DataFrame a una lista de diccionarios
        json_data = df.to_dict(orient='records')

        # Define el nombre del archivo JSON de salida
        nombre_json = archivo_xlsx.replace('.xlsx', '.json')

        # Guarda la lista de diccionarios en un archivo JSON
        with open(nombre_json, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)

        return f'Se ha creado el archivo JSON: {nombre_json}'
    except Exception as e:
        return f'Error al procesar {archivo_xlsx}: {str(e)}'


# Procesa los archivos en paralelo para mayor eficiencia
with concurrent.futures.ThreadPoolExecutor() as executor:
    resultados = list(executor.map(procesar_xlsx, archivos_xlsx))

# Imprime los resultados
for resultado in resultados:
    print(resultado)
