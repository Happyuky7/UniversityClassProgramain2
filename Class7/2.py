# 1.1 Dibujar la frecuencia en histograma
"""
Se le solicita al usuaraio ingresar un texto, el programa debe generar un historgrama, considerando solo las vocales.

Definir los pasos para hacer un histograma:
1. Solivitar al usuario que ingrese una palabra
2. Lleve todo el texto a minusculas, usando el metodo `.lower()`
3. Encontrar la cantidad de letras del texto ingresado por el usuario
4. Hay que usar un ciclo `for` para recorrer todo la cadena de texto
5. Luego compara cada letra con las vocales, si son iguales debemos agregar un `*`
"""

def draw_histogram(text):
    vowels = "aeiouáéíóú"
    text = text.lower()
    for letter in text:
        if letter in vowels:
            print("*", end="")
        else:
            print(" ", end="")

while True:

    try: 
        
        text = input("Ingrese una palabra: ")
        draw_histogram(text)
        print()
        print("Frecuencia en histograma:")
        count = text.count("a") + text.count("e") + text.count("i") + text.count("o") + text.count("u")
        print(f"Vocales: {count}")
        print(f"Consonantes: {len(text) - count}")
        print(f"Total: {len(text)}")
        print()

        if input("¿Desea continuar? (y/n): ").lower() != "y":
            break

    except ValueError:

        print("Error: Los valores ingresados son incorrectos.")
        continue