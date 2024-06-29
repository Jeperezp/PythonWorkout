"""
•	Especificación: Crea un programa que simule el registro de usuarios. El programa debe solicitar al usuario que ingrese su nombre de usuario y contraseña, verificar si ya existe un usuario con ese nombre, y escribir la información en un archivo de texto.
•	Manejo de errores: Maneja errores relacionados con el registro de usuarios duplicados o problemas al escribir en el archivo.
"""

import json
import re

opciones = {
    1:"Registro",
    2:"Ingreso",
    3:"Salir"
}

print("Selecciones alguna de estas opciones")
for i,j in opciones.items():
    print(i, j)

opcion = 0
while opcion not in [1,2,3]:
    entrada_valida = False
    while not entrada_valida:
        try:
            opcion = int(input('Ingrese el número de la opción: '))
            if opcion not in [1,2,3]:
                print('Opción ingresada no se encuentra registrada en el catálogo, vuelve a intentarlo')
                for i,j in opciones.items():
                    print(i, j)
            else:
                entrada_valida = True
        except ValueError:
            print('Se ha ingresado un valor no válido. Por favor,las opciones son:')
            for i,j in opciones.items():
                print(i, j)

def validar_usuario(Nombre, usuario,correo):
        if re.match(r'^[a-zA-Z]+$', Nombre) and re.match(r'^[a-zA-Z]+$', usuario) and re.match(r'^[\w\.-]+@[\w\.-]+$', correo):
            return True
        else:
            return False

if opcion==3:
    print('Gracias')
    exit()
else:
    Nombre = input('Ingrese su Nombre').lower()
    usuario = input('Ingrese su usuario').lower()
    correo = input('Ingrese su usuario').lower()


match opcion:
    case 1:
        if validar_usuario(Nombre, usuario,correo)==False:
            print('Alguno de los Datos no Cumple con la estructura, por favor validar')
        try:
            with open('Registros.json','r') as Registros_bd:
                Registros = json.load(Registros_bd)

            for registro in Registros:
                if registro.get('correo') ==correo:
                    print('El correo ya esta registrado en la Base, y no se puede registrar nuevamente')
                    break
                else:
                    registro_nuevo = {
                        "Nombre":Nombre,
                        "Usuario":usuario,
                        "Correo":correo
                    } 
                    Registros.append(registro_nuevo)
                    with open('Registros.json', 'w') as Registros:
                        json.dump(Registros, Registros, indent=4)      

        except FileNotFoundError:
            print('Base de registros No Encontrada')

    case 2:
        if validar_usuario(Nombre, usuario,correo)=="Estructura no Cumple":
            print('Alguno de los Datos no Cumple con la estructura, por favor validar')
        try:
            with open('Registros.json','r') as Registros_bd:
                Registros = json.load(Registros_bd)
            for registro in Registros:
                if registro.get('correo') ==correo:
                    print('Bienvenido')
                else:
                    print('El correo Ingresado no se encuentra registrado, por favor vuelva a intentarlo')
                    break
        except FileNotFoundError:
            print('Base de registros No Encontrada')




