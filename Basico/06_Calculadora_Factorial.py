"""
Escribe un programa que calcule el factorial de un número ingresado por el usuario
"""

n = 23
fact = 1

for i in range(1,n+1):
    fact = fact*i

print(f'{"Numero Factorial de":10} {n} es {fact}')