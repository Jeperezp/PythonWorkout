"""
 Crea un programa que ordene una lista de números ingresada por el usuario, 
 ya sea de forma ascendente o descendente.
"""

lista = [100, 45, 101, 27, 32, 37, 1]
lista_ordenada = []

while lista:
    minimo = lista[0]
    print(minimo)
    for num in lista:
        print(num)
        if num < minimo:
            print(num)
            print(minimo)
            minimo = num
    
    lista_ordenada.append(minimo)
    lista.remove(minimo)