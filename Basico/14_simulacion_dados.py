"""
Crea un programa que simule el lanzamiento de dados, 
permitiendo al usuario especificar el número de dados y el número de caras por dado.
"""
import random

can_dados = int(input('Ingrese la cantidad de dados'))
can_caras = int(input('Ingrese la cantidad de caras de los dados'))

for dado in range(can_dados):
    print(f"La cantidad para el dado numero {dado+1} es {random.randint(1,can_caras)}")

