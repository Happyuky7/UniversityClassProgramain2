# 3.1 Tabla de multiplicar, usando for
#
# Mostrar la tabla de multiplicar de un numero entero introducida por el usuario.
# Hasta el numero ingresado x 10.

while True:

    try: 

        numero = int(input("Ingrese un número entero: "))

        for i in range(numero):
            print(f"{numero} x {i+1} = {numero * (i+1)}")
            if i == 11:
                break


        if input("¿Desea continuar? (y/n): ").lower() != "y":
            break

    except ValueError:

        print("Error: Los valores ingresados son incorrectos.")
        continue