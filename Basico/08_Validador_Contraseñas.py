"""
Desarrolla un programa que valide si una contraseña ingresada por el usuario cumple con ciertos criterios, 
como longitud mínima, uso de caracteres especiales
"""
#Longitud mayor a 10 caracteres
#Alfanumerico
#Caracteres Especiales
#Mayuscula

import re
contraseña = "Ae!4gV2her*"
patron = r"^(?=.*[!@#$%^&*()-_=+])(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{10,}$"

if not re.match(patron, contraseña):
    print("La contraseña no cumple con los criterios de seguridad.")
else:
    print("La contraseña es válida.")