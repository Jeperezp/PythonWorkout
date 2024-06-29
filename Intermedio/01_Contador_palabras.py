"""
Especificación: Crea un programa que lea un archivo de texto y cuente la frecuencia de cada palabra. Luego, escribe los resultados en un nuevo archivo de texto.
Manejo de errores: Maneja los posibles errores al abrir o leer el archivo
"""

from collections import Counter
import string, os

os.getcwd()

with open('Intermedio\\Fragmento.txt', 'r',encoding='utf-8') as archivo:
    contenido = archivo.read()

def analizar_texto(texto):

    texto_limpio = texto.translate(str.maketrans('', '', string.punctuation)).lower()
    palabras = texto_limpio.split()

    cantidad_palabras = len(palabras)
    longitud_promedio = sum(len(palabra) for palabra in palabras) / cantidad_palabras

    longitud_maxima = max(len(palabra) for palabra in palabras)
    longitud_minima = min(len(palabra) for palabra in palabras)

    frecuencia_palabras = Counter(palabras)

    return {
        "cantidad_palabras": cantidad_palabras,
        "longitud_promedio": longitud_promedio,
        "longitud_maxima": longitud_maxima,
        "longitud_minima": longitud_minima,
        "frecuencia_palabras": frecuencia_palabras
    }

resultado = analizar_texto(contenido)

print("Cantidad de palabras:", resultado["cantidad_palabras"])
print("Longitud promedio de las palabras:", resultado["longitud_promedio"])
print("Longitud máxima de las palabras:", resultado["longitud_maxima"])
print("Longitud mínima de las palabras:", resultado["longitud_minima"])
print("Frecuencia de palabras:", resultado["frecuencia_palabras"])