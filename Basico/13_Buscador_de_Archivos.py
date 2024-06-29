"""
Desarrolla un programa que busque archivos con una extensión específica en un 
directorio proporcionado por el usuario.
"""

import os

ruta = input('Ingrse la ruta a consultar')
tipo_archivo = input('Ingrese la extension del archivo que desea buscar')

archivos = os.listdir(ruta)

archivos_filtrados = [archivo for archivo in archivos if archivo.endswith(tipo_archivo)]

for archivo in archivos_filtrados:
    print(os.path.join(ruta, archivo))