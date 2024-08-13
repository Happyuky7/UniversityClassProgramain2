# Comprobar si eres mayor de edad en usando una funcion

def more_age(age):
    try:
        age = int(age)
        if age >= 18:
            return print("Eres mayor de edad.")
        else:
            return print("Eres menor de edad.")
    except ValueError:
        return "Error: La edad ingresada no es un número."
    
while True:

    try: 

        age = input("Ingrese su edad: ")
        more_age(age)

        print("")

        if input("¿Desea continuar? (y/n): ").lower() != "y":
            break

    except ValueError:

        print("Error: Los valores ingresados son incorrectos.")
        continue