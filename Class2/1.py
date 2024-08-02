#1.9 Escriba un problema que calcule la velocidad promedio de un objecto, usando la formula 
# vpromedio = delta x / delta t, el usuario debe ingresar los valores necesarios.

# Formula: Vp= Δx/Δt

def calculate_velocity_average(distance, time):

    velocity_average = distance / time
    return velocity_average

while True:

    try: 

        distance = float(input("Ingrese la distancia recorrida (en metros): "))
        time = float(input("Ingrese el tiempo transcurrido (en segundos): "))

        velocity_average = calculate_velocity_average(distance, time)

        print(f"La velocidad promedio es: {velocity_average} m/s")

        if input("¿Desea calcular otra velocidad promedio? (y/n): ") != "y":
            break

    except ValueError:

        print("Error: Debe ingresar valores numéricos.")
        continue


