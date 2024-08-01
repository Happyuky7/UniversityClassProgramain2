
# Empresa de cuenta de subscripción

iva = 0.81 # 19%

while True:
    price = 0
    try:
        price = int(input("Precio de Subscripción: "))
        users = int(input("Numero de Usuarios que contratan el servicio: "))
        gastos = int(input("Gastos Operacionales: "))

        utilidad = (price * users) - gastos
        utilidaes_finales = utilidad * 0.19

        print(F"Utilidades: ${utilidaes_finales}")

        bucle = str(input("Deseas hacer otro cálculo? (y/n): "))
        if bucle.lower() == "y":
            pass
        else:
            exit()


    except ValueError:

        print("No es un numero.")
        pass


