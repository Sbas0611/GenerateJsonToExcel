import json
import pandas as pd

# Lee el archivo Excel en un DataFrame de pandas
# Reemplaza 'archivo.xlsx' con el nombre de tu archivo Excel
excel_file = 'data/colores.xlsx'
df = pd.read_excel(excel_file)

# Convierte el DataFrame a una lista de diccionarios
json_data = df.to_dict(orient='records')

# Guarda la lista de diccionarios en un archivo JSON
# Reemplaza 'archivo.json' con el nombre que desees para el archivo JSON
json_file = 'archivo.json'
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

print(f'Se ha creado el archivo JSON: {json_file}')
