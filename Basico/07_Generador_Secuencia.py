"""
Crea un programa que genere una secuencia de números, 
como los primeros N números pares o los primeros N términos de la serie Fibonacci.
"""

opcion = 2
Inicio = 1
Final= 100
Cantidad_n = 10

lista = []
lista_fibo = [0,1]
match opcion:
    case 1:
        for i in range(Inicio,Final):
            if i%2==0:
                lista.append(i)
            if len(lista)>Cantidad_n:
                break
        print(lista)
    case 2:
        for i in range(0,Cantidad_n-2):           
            lista_fibo.append(lista_fibo[-1]+lista_fibo[-2])
        print(lista_fibo)        
        