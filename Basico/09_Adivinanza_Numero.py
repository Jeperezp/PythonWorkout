"""
Escribe un programa que genere un número aleatorio y le dé al usuario la oportunidad de adivinarlo, 
proporcionando pistas si el número es mayor o menor.
"""
import random

num = random.randint(1,100)

print(f'{"Bienvenido al Juego de Adivina el Numero":40}')
print(f'Solo tienes 3 Oportunidades')

for i in range(1,4):
    valor = int(input('Ingresa un Numero entre 1 y 100 '))
    if valor >num:
        print('el Numero a adivinar es menor al que escribiste')
    elif valor<num:
        print('El Numero a adivinar es mayor al que escribiste')
    else:
        valor ==num
        print('Felicitaciones Haz Ganado')
        break