"""
Escribe un programa que genere contraseñas seguras de forma aleatoria, 
permitiendo al usuario especificar la longitud y los tipos de caracteres a incluir.
"""

import re
import string
import random

longitud = int(input('Ingrese la longitud de la contraseña'))
#patron = r"^(?=.*[!@#$%^&*()-_=+])(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{10,}$"
patron = r"^(?=.*[!@#$%^&*()-_=+])(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{" + str(longitud) + r",}$"

control = 1
while control==1:
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    if re.match(patron, contrasena):
        print("La contraseña es válida.")
        print(contrasena)
        control =2

"""-------------------------------------Funcion-------------------------------------------------------"""

def Generador (longitud:int):
    # 1 es Activo
    # 2 es Finalizado
    patron = r"^(?=.*[!@#$%^&*()-_=+])(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{" + str(longitud) + r",}$"
    Activo = 1
    while Activo==1:
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
        if re.match(patron, contrasena):
            Activo =2
            return contrasena

            