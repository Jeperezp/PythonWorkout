"""
Escribe un programa que calcule el área y el perímetro de diferentes formas geométricas, 
como círculos, triángulos o cuadrados.
"""
import math

Medidas = {
    1:"Triangulo",
    2:"Circulo",
    3:"Cuadrado",
    4:"Rectanculo"
    }
print(f'{'Bienvenido':^40}')
print(f'{"Por Favor Seleccione una Opcion "}')

for k, j in Medidas.items():
    print(f"Opcion {k}: {j}")

Num = int(input('Ingrese un Numero de las opciones Anteriormente Mencionadas'))

match Num:
    case 1:
        print('Para Calcular el Area y Perimetro del Triangulo Requiero me ayudes con los siguientes Datos, ingresandolos en el siguiente orden Base, ')
        Lados = []
        for i in range(1,4):
            Lados.append(input(f'Ingresa la {i} medida'))
        Lados = list(map(float,Lados))
        print(f'{"El Perimetro del Triangulo es:":40} {sum(Lados)}')
        s= (Lados[0]+Lados[1]+Lados[2])/2
        area = (s*(s-Lados[0]) * (s-Lados[1])*(s-Lados[2]))**(1/2)
        print(f'El Area del Triangulo es: {area}')
    case 2:
        print('Para Calcular el Area y perimetro de un circulo requiero el Radio del circulo ')
        r = int(input('Ingrese el Radio del Circulo: '))
        area = math.pi() *(r**2)
        perimetro = 2 * math.pi()*r
        print(f'{"El Area del Circulo es":40} {area}')
        print(f'{"El perimetro del Circulo es":40} {perimetro}')
    case 3:
        print('Para Calcular el Area y perimetro de un Cuadrado requiero me suministres')
        l = int(input('Ingrese la longitud de un lado: '))
        area = l**2
        perimetro = l*4
        print(f'{"El Area del cuadrado es":40} {area}')
        print(f'{"El perimetro del Cuadrado es":40} {perimetro}')
    case 4:
        print('Para Calcular el Area y perimetro de un rectangulo requiero me suministres')
        b = int(input('Ingrese la longitud de la base: '))
        a = int(input('Ingrese la longitud de la altura : '))
        area = b*a
        perimetro = (2*b) + (2*a)
        print(f'{"El Area del cuadrado es":40} {area}')
        print(f'{"El perimetro del Cuadrado es":40} {perimetro}')


