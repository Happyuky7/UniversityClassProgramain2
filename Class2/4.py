# Estructuras de control.
# 2.1 Días de la semana:
# Realizar un programa, que le pregunte al usuario que día es y luego en pantalla imprimir si es un día labolar o no.

def is_weekday(day_name):
    
    weekdays = ["lunes", "martes", "miércoles", "jueves", "viernes", "sabado", "domingo"]

    if day_name.lower() in weekdays:
        return True
        
    return False
        


def day_laboral(day_name):
    
    laboral_list = ["lunes", "martes", "miércoles", "jueves", "viernes"]
    if day_name.lower() in laboral_list:
        print(f"El día {day_name} es laboral.")
    else:
        print(f"El día {day_name} no es laboral.")

while True:

    try: 

        day_name = input("Ingrese el día de la semana (nombre completo): ")

        if is_weekday(day_name):
            day_laboral(day_name)
        else:
            print(f"El día ingresado no es un día de la semana.")
            

        if input("¿Desea continuar? (y/n): ").lower() != "y":
            break

    except ValueError:

        print("Error: Los valores ingresados son incorrectos.")
        continue