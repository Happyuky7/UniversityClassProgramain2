# 3.3 Archivo 
"""
Crear una función que cree un archivo, con un nombre ingresado por el usuario (como parametro de entrada),
todos los archivos que crea esta funcion deben contener 3 lineas, cada linea contiene un numero aletatorio.
"""

import random

def random_number():
    return random.randint(0, 1000)

def create_file(filename):
    with open(f"{filename}.txt", "w", encoding="utf-8") as file:
        for i in range(3):
            number = random_number()
            file.write(f"{number}\n")

while True:

    try: 

        filename = input("Ingresa el nombre del archivo que quieres generar: ")
        create_file(filename)
        print(f"Archivo '{filename}.txt' creado con éxito.")

        if input("¿Desea continuar? (y/n): ").lower() != "y":
            break

    except ValueError:

        print("Error: Los valores ingresados son incorrectos.")
        continue