import numpy as np
import matplotlib.pyplot as plt
import random


def main():

    lista = [31,28,29,19]
    print(lista)

    print(lista[0])

    arr = np.array(lista)
    print(arr)

    lista_2d = [[2,3,4],
                [3,4,5],
                [3,3,5],
                [3,4,5]]
    
    print(lista_2d)
    print(lista_2d[0])

    arr2d = np.array(lista_2d)
    print(f"El elemento 0 es: {arr2d[0]}")

    x = np.arange(0,25,3)
    print(x)

    as2 = np.linspace(0,10,145)
    print(as2)

    a2 = np.logspace(0,10,11, base=np.e)
    print(a2)

    M1 = random.rand(3,3)
    print(f"Matriz aleatoria 1:\n{M1}")


if __name__ == "__main__":
    main()