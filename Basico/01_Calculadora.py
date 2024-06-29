"""
Crea un programa que solicite dos números al usuario y realice operaciones básicas como: 
suma, resta, multiplicación y división
"""
print(f'Bienvenido, por favor selecciona la operacion que quieres realizar:\n\n{"1":10}{"Suma":10}\n{"2":10}{"Resta":10}\n{"3":10}{"Multiplicacion":10}\n{"4":10}{"Division":10}')
Numero = int(input('Selecciona la Operacion que quieres Realizar'))
N1 = int(input('Ingrese el Primer Valor'))
N2 = int(input('Ingrese el Segundo Valor'))

match Numero:
    case 1:
        print(f"El resultado de la suma de {N1} y {N2} es {N1+N2}")
    case 2:
        print(f"El resultado de la Resta de {N1} y {N2} es {N1-N2}")        
    case 3:
        print(f"El resultado de la Multiplicacion de {N1} y {N2} es {N1*N2}")
    case 4:
        print(f"El resultado de la Division de {N1} y {N2} es {N1/N2}")

