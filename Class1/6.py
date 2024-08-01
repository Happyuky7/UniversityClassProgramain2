
iva = 0.81 # 19%

while True:
    price = 0
    try:
        price = int(input("Precio de Subscripción: "))
        users = int(input("Numero de Usuarios Totales (premium + free + normal): "))
        premium = int(input("Numero de Usuarios Premium: "))
        free = int(input("Numero de Usuarios Free: "))
        gastos = int(input("Gastos Operacionales: "))

        users_normal = int(((premium + free) - users))

        price_normal = price * 1

        price_premium = price * 2

        sumatoria = (price_premium*premium) + (price_normal*users_normal) 
        
        utilidad = sumatoria - gastos

        utilidaes_finales = utilidad * iva

        print(f"Users Normales: ${users_normal}")
        print(f"Utilidades: ${utilidaes_finales}")

        bucle = str(input("Deseas hacer otro cálculo? (y/n): "))
        if bucle.lower() == "y":
            pass
        else:
            exit()


    except ValueError:

        print("No es un numero.")
        pass


