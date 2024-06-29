"""
Crea un programa que analice un texto ingresado por el usuario y proporcione estadísticas como la cantidad de palabras, 
la longitud promedio de las palabras, etc.
"""

from collections import Counter
import string

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

texto = "Crea un programa que analice un texto ingresado por el usuario y proporcione estadísticas como la cantidad de palabras, la longitud promedio de las palabras, etc."
resultado = analizar_texto(texto)

print("Cantidad de palabras:", resultado["cantidad_palabras"])
print("Longitud promedio de las palabras:", resultado["longitud_promedio"])
print("Longitud máxima de las palabras:", resultado["longitud_maxima"])
print("Longitud mínima de las palabras:", resultado["longitud_minima"])
print("Frecuencia de palabras:", resultado["frecuencia_palabras"])