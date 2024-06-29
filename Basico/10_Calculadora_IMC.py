"""
Desarrolla un programa que calcule el índice de masa corporal (IMC) de una persona a partir de su peso y altura.
"""

Altura = input('Ingrese Su altura en Metros')
Peso = input('Ingrese Su peso en Kilogramos')

Altura = float(Altura)
Peso = float(Peso)

IMC = Peso/(Altura**2)

if IMC <18.5:
    print(f'{IMC} Bajo de Peso')
elif IMC <24.9:
    print(f'{IMC} Normal')
elif IMC <29.9:
    print(f'{IMC} Sobrepeso')
else:
    print(f'{IMC} Obsesidad')
