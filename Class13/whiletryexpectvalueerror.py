# Esto esta pensado para hacer un copy paste y modificar el código para que ya tenga la opción de continuar o no

while True:

    try: 

        if input("¿Desea continuar? (y/n): ").lower() != "y":
            break

    except ValueError:

        print("Error: Los valores ingresados son incorrectos.")
        continue