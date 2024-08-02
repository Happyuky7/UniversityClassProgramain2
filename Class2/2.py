# 1.10 Escriba un programa que reciba dos posiciones de un plano carteciano (X,Y) y calcule la distancia entre los dos puntos.

def get_distance(x1, y1, x2, y2):

    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
    return d

while True:
    try:
        x1 = float(input("Ingrese la posición X1: "))
        y1 = float(input("Ingrese la posición Y1: "))

        print("---------------------------------")

        x2 = float(input("Ingrese la posición X2: "))
        y2 = float(input("Ingrese la posición Y2: "))

        print("---------------------------------")

        distance = get_distance(x1, y1, x2, y2)

        print(f"La distancia entre los puntos ({x1}, {y1}) y ({x2}, {y2}) es: {distance:.2f} unidades")

        if input("¿Desea calcular otra velocidad promedio? (y/n): ") != "y":
            break

    except ValueError:
        print("Los valores ingresados deben ser numéricos.")