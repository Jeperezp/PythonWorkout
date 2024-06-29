"""Desarrolla un programa que determine si un número ingresado por el usuario es primo o no."""
Numero = int(input("Introduzca el numero a evaluar"))

if Numero<2:
    print('No es Numero Primo')
for i in range(2,int(Numero**0.5)+1):
    if Numero%i ==0:
        print('No es Numero Primo')
        break
    else:
        print('Es Numero Primo')


