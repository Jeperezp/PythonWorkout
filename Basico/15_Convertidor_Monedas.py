
Monedas = {
    1:["COP - USD",1,0.00026],
    2:["COP - CAD",1,0.00035],
    3:["COP - MXN",1,0.044],
    4:["MXN - USD",1,0.058],
    5:["MXN - CAD",1,0.081],
    6:["USD - CAD",1,1.38],
    7:["USD - EUR",1,0.94],
    8:["COP - EUR",1,0.00024],
    9:["CAD - EUR",1,0.68],
    10:["MXN - EUR",1,0.055]    
}

print(f'{'Bienvenido':^40}')
print(f'{"Por Favor Seleccione una Opcion "}')

for k, j in Monedas.items():
    print(f"Opcion {k}: {j[0]}")

opcion = int(input('Ingrese la opcion que se ajuste a la necesidad'))

match opcion:
    case 1:
        monto = float(input('Ingrese la cantidad de Pesos a Convertir'))
        conversion = (Monedas[opcion][1] * monto) *Monedas[opcion][2]
        print(f"El monto ingresado en USD es de: {conversion}")
    case 2:
        monto = float(input('Ingrese la cantidad de Pesos a Convertir'))
        conversion = (Monedas[opcion][1] * monto) *Monedas[opcion][2]
        print(f"El monto ingresado en CAD es de: {conversion}")
    case 3:
        monto = float(input('Ingrese la cantidad de Pesos a Convertir'))
        conversion = (Monedas[opcion][1] * monto) *Monedas[opcion][2]
        print(f"El monto ingresado en MXN es de: {conversion}")
    case 4:
        monto = float(input('Ingrese la cantidad de Pesos Mexicanos a Convertir'))
        conversion = (Monedas[opcion][1] * monto) *Monedas[opcion][2]
        print(f"El monto ingresado en USD es de: {conversion}")
    case 5:
        monto = float(input('Ingrese la cantidad de Pesos Mexicanos a Convertir'))
        conversion = (Monedas[opcion][1] * monto) *Monedas[opcion][2]
        print(f"El monto ingresado en CAD es de: {conversion}")
    case 6:
        monto = float(input('Ingrese la cantidad de Dolares Americanos a Convertir'))
        conversion = (Monedas[opcion][1] * monto) *Monedas[opcion][2]
        print(f"El monto ingresado en CAD es de: {conversion}")
    case 7:
        monto = float(input('Ingrese la cantidad de Dolares Americanos a Convertir'))
        conversion = (Monedas[opcion][1] * monto) *Monedas[opcion][2]
        print(f"El monto ingresado en EUR es de: {conversion}")
    case 8:
        monto = float(input('Ingrese la cantidad de Pesos a Convertir'))
        conversion = (Monedas[opcion][1] * monto) *Monedas[opcion][2]
        print(f"El monto ingresado en EUR es de: {conversion}")
    case 9:
        monto = float(input('Ingrese la cantidad de dolares Canadiences a Convertir'))
        conversion = (Monedas[opcion][1] * monto) *Monedas[opcion][2]
        print(f"El monto ingresado en EUR es de: {conversion}")
    case 10:
        monto = float(input('Ingrese la cantidad de Pesos Mexicanos a Convertir'))
        conversion = (Monedas[opcion][1] * monto) *Monedas[opcion][2]
        print(f"El monto ingresado en EUR es de: {conversion}")

"------------------------------------Conversion de Monedas con una Funcion-------------------------------------"

def conversion (opcion:int,monto:float):
    return f" el monto ingresado para convertir de {Monedas[opcion][0]} es {Monedas[opcion]}({(Monedas[opcion][1] * monto) *Monedas[opcion][2]})"

    