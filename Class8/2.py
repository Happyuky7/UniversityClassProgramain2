# 3.2 Cuenta regresiva
"""
Generar una función que imprima en pantalla una cuenta regresiva de un valor ingresado por el usuario (en segundos):
cuando el contanodr llegue a cero debe imprimir en pantalla "Booon!"
"""

import time
import os


def countdown(seconds):
    while seconds >=0:
        print(seconds)
        seconds -= 1
        time.sleep(1)
        if seconds == 0:
            time.sleep(2)
            os.system('cls')
            print('Booon!')
            break


while True:

    try: 

        seconds = int(input("Ingrese un número entero positivo: "))
        if seconds <= 0:
            print("Debe ingresar un número entero positivo.")
            continue
        countdown(seconds)


        if input("¿Desea continuar? (y/n): ").lower() != "y":
            break

    except ValueError:

        print("Error: Los valores ingresados son incorrectos.")
        continue