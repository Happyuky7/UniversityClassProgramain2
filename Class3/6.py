# 3.6 La letra t en funcion
# Dibuje una letra t con asteriscos.

def draw_letter_t(n):
    elemento = '*'
    punto_medio = int(n / 2)
   
    for i in range(n):
        if i == 0:
            print(elemento * n)
        else:
            print(" " * punto_medio + elemento)

while True:

    try: 

        n = int(input("Ingrese el tamaño de la letra t: "))

        if n <= 0:
            print("Error: El valor ingresado es incorrecto.")
            continue

        print(" ")
        draw_letter_t(n)
        print(" ")


        if input("¿Desea continuar? (y/n): ").lower() != "y":
            break

    except ValueError:

        print("Error: Los valores ingresados son incorrectos.")
        continue