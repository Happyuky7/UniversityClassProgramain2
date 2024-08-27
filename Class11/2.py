# 10.3 Jugando con listas
"""
Escriba una funcion llamada "miFuncion(lista1, lista2)" que recibe como entrada las siguientes dos listas

nombres = ["Felipe","Ana","Juan","Natalia","Rodrigo","Mauricio"]
numeros = [315,200,400]

La primera lista corresponde a una lista de nombres y la segunda lista a una lista con numeros
enteros. A partir de la lista nombres, la funcion deberá contar cuyos nombres tengan más de 3
vocales y multiplicar este número obtenido, por cada uno de los elementos numéricos de la lista2.
La funcion deberá retornar una nueva lista, con los valores nuebos. La lista original números, no
debe ser modificada.
"""

nombres = ["Felipe","Ana","Juan","Natalia","Rodrigo","Mauricio"]
numeros = [315,200,400]

def miFuncion(lista1: list, lista2: list):

    try:

        vowels = "aeiouAEIOU"
        new_list = []
        
        for name in lista1:
            count = 0
            for letter in name:
                if letter in vowels:
                    count += 1
            if count > 3:
                for number in lista2:
                    new_list.append(count * number)
        return new_list
    
    except Exception as e:
        return e

def main():

    print(miFuncion(nombres, numeros))

if __name__ == "__main__":
    main()