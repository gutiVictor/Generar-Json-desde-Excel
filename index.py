import pandas as pd
import json


excel_file = 'libro1.xlsx'  # Ruta del archivo Excel cambiar con el nombre 

# Leer la hoja del archivo Excel (asumiendo que la primera fila son encabezados)
df = pd.read_excel(excel_file, header=None)

# Crear un diccionario a partir del DataFrame
productos_dict = {}


for index, row in df.iterrows():
    # Aquí asignamos el primer valor (código) como clave principal del diccionario
    productos_dict[str(row[0])] = {
        "descripcion": row[1],  # La segunda columna (row[1]) es la descripción
        "ref": row[2]           # La tercera columna (row[2]) es la referencia
    }

# Guardar el diccionario como archivo JSON
with open('productos.json', 'w', encoding='utf-8') as json_file:
    json.dump(productos_dict, json_file, ensure_ascii=False, indent=4)

print("Archivo JSON generado exitosamente.")
