# 10.1 Virus T
"""
El **"Virus T"** ha infectado aa una cierta canntidad de personas en la ciudad de Springfield. Se ha registrado en dos listas
(relacionadas 1:1), la cantidad de personas involucrafas en esta situación y su estado de infección tal y como se muestra a continuación:

nombres = ["Juan", "Diego", "Felipe", "Natalia", "Pedro", "Adin", "Anibal"]
estado = [1,1,1,0,0,1,0]

El estado de infección se ha catalogado con un número, donde un 1 representa una persona infectada y un 0 como una
persona no infectado. Se le solicita a usted que elabore una función llamada **infectados(a,b)** que retorne el porcentaje de
infectados tal y como se muestra a continuación. Debe utilizar el mismo formato de salida que se ve en el siguiente ejemplo
(con 1 decimal y el simbolo de porcentaje).
"""

nombres = ["Juan", "Diego", "Felipe", "Natalia", "Pedro", "Adin", "Anibal"]
estado = [1,1,1,0,0,1,0]

def infectados(a,b):

    infectados = 0
    no_infectados = 0

    for i in range(len(a)):
        if b[i] == 1:
            infectados += 1
        else:
            no_infectados += 1
    return f"{(infectados / (infectados + no_infectados)) * 100:.1f}%"

def main():

    print( )
    print(f"El porcentaje de infectados es de: {infectados(nombres, estado)}")
    print( )

if __name__ == "__main__":
    main()