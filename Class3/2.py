# 2.2 IF Y ELSE
# Calculando el procentaje de victorias:
#
# Valores de entrada
# - Numero de juegos ganados
# - Numero de juego empleados
# - Numero de juegos perdidos
#
# Se debe entregar:
# - Los juegos Totales
# - El porcentaje de victorias
# 
# El procentaje de victorias sigue las siguientes reglas:
# - Si los empates son iguales a cero: se calula como la division entre juegos ganados y juegos totales multiplicado por 100.
# - Si los empates son iguales de cero (positivo), entonces el porcentaje de vistorias se calula considerando que un empate, 
# es equivalente a media victoria, lo que se suma al total de victorias, para divirse con los juegos totales y 
# luego se multiplican por 100.


while True:

    try: 

        n_juegos_ganados = int(input("Ingrese el numero de juegos ganados: "))
        n_juegos_empatados = int(input("Ingrese el numero de juegos empatados: "))
        n_juegos_perdidos = int(input("Ingrese el numero de juegos perdidos: "))

        n_juegos_totales = n_juegos_ganados + n_juegos_empatados + n_juegos_perdidos

        if n_juegos_empatados == 0:

            porcentaje_victorias = (n_juegos_ganados / n_juegos_totales) * 100
            print(f"Los juegos Totales: {n_juegos_totales}")
            print(f"El porcentaje de victorias: {porcentaje_victorias:.2f}%")

        elif n_juegos_empatados > 0:

            n_juegos_ganados += n_juegos_empatados / 2
            porcentaje_victorias = (n_juegos_ganados / n_juegos_totales) * 100
            print(f"Los juegos Totales: {n_juegos_totales}")
            print(f"El porcentaje de victorias: {porcentaje_victorias:.2f}%")

        else:
            print("Error durante el calculo de los porcentajes de victorias.")

        if input("¿Desea continuar? (y/n): ").lower() != "y":
            break

    except ValueError:

        print("Error: Los valores ingresados son incorrectos.")
        continue