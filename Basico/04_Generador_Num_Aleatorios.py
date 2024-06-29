"""
Crea un programa que genere un número aleatorio entre un rango especificado por el usuario.
"""
import random

Num1 = int(input('Ingrese el Primer valor '))
Num2 = int(input('Ingrese el segundo valor '))

if Num1 <0 or  Num2<0:
    print('Por Favor Validar el Numero Recibido, solo se permiten numeros positivos')
else:
    print(random.randint(Num1,Num2))
