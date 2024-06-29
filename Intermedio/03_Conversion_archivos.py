"""
Especificación: Crea un programa que convierta un archivo de texto en formato CSV a formato JSON y viceversa. El programa debe manejar ambos tipos de archivos de entrada y salida.
Manejo de errores: Verifica la validez del formato de entrada y maneja errores al abrir o escribir archivos.
"""

import pandas as pd

def csv_to_json(name_file):
    name = name_file.split('.')
    if name[1]=='csv':
        try:
            df = pd.read_csv(name_file)
            return df.to_json(name[0]+'.json',orient='records',indent = 4)
        except Exception as e:
            return f"Error: {e}"
    elif name[1]=='json':
        try:
            df = pd.read_json(name_file)
            return df.to_csv(name[0]+'.csv',sep = ';',index=False)
        except Exception as e:
            return f"Error: {e}"        
    else:
        return "El formato del Archivo no corresponde a Json o csv"
    
csv_to_json('Datos.json')
