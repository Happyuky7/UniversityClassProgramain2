# 2.4 Media Aritmetica (Promedio)
#
# Escribir un programa que pida al usuario un numero a la vez, 
# el usuario debe ingresar un criterio de parada que se ingrese desde pantalla.

i = []
media = float(0.0)

while True:
    try:
        numero = float(input("Ingrese un número, si es decimal use '.' (o '-1' para terminar): "))
        if numero == -1:
            break
        
        i.append(numero)
        media = sum(i) / len(i)

        
    except ValueError:
        print("Error: Ingreso incorrecto. Ingrese un número.")

print(f"La media aritmetica de los números ingresados es: {media:.1f}")