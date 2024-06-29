"""
Desarrolla un programa que convierta entre diferentes unidades, 
como de Celsius a Fahrenheit o de kilómetros a millas.
"""
Medidas = {
    1:["Centimetros", "Metros"],
    2:["Metros","Kilometros"],
    3:["Kilometros", "Millas"],
    4:["Centigrados", "Fahrenheit"],
    5:["Fahrenheit","Kelvin"]
    }
print(f'{'Bienvenido':^40}')
print(f'{"Por Favor Seleccione una Opcion"}')

for k, j in Medidas.items():
    print(f"Opcion {k}: {j[0]} a {j[1]}")

Numero =int(input('Ingrese el Numero de la Opcion que requiere'))

match Numero:
    case 1:
        valor1 = int(input('Ingrese el valor'))
        print(f'{"El resultado es":40} Centimetros: {valor1:5}  Metros: {(valor1/100):5}')
    case 2:
        valor1 = int(input('Ingrese el valor'))
        print(f'{"El resultado es":40} Metros: {valor1:5}  Kilometros: {(valor1/1000):5}')    
    case 3:
        valor1 = int(input('Ingrese el valor'))
        print(f'{"El resultado es":40} Kilometro: {valor1:5}  Milla: {(valor1/1609):5}') 
    case 4:
        valor1 = int(input('Ingrese el valor'))
        print(f'{"El resultado es":40} Celsius: {valor1:5}  Fahrenheit: {((valor1*(9/5))+32):5}') 
    case 5:
        valor1 = int(input('Ingrese el valor'))
        print(f'{"El resultado es":40} Fahrenheit: {valor1:5}  Kelvin: {((valor1-32)*5/9)+273.15:5}') 


