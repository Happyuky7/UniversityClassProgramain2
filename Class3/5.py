# 3.4 Dibuje un rectangulo con *

def draw_rectangle(a, b):
    elemento = '*'
    base = elemento * b
    for _ in range(a):
        print(base)
    
while True:

    try: 

        a = int(input('Ingrese el alto del rectángulo: '))
        b = int(input('Ingrese el ancho del rectángulo: '))

        print(" ")

        draw_rectangle(a, b)

        print(" ")

        if input("¿Desea continuar? (y/n): ").lower() != "y":
            break

    except ValueError:

        print("Error: Los valores ingresados son incorrectos.")
        continue