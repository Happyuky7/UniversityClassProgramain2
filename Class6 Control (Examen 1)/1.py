# 7 Leer algunas lineas
"""
Generar un archivo de texto simple de 10 lineas | 1.1

- Leer del archivo las primeras 5 lineas | 1.2
- Leer de un archivo de la tercera a la septima linea | 1.3
- leer el archivo y contar la cantidad de lineas que contiene (usar un contador) | 1.4
- leer el archivo y contar la cantidad de caracteres (usar len) | 1.5
- leer el archivo y contar la cantidad de palabras que contienen (usar split) | 1.6
- Leer el archivo y copiar el contenido a otro, pero solo hasta la linea 5 | 1.7
"""

with open("file.txt", "w", encoding="utf-8") as file:
    for i in range(10):
        file.write(f"Linea{i+1}\n")
    print("Archivo creado con exito!")
    
print("\n================================")

print("Las primeras 5 lineas del archivo son:")
with open("file.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for i in range(5):
        print(lines[i])

print("\n================================")

print("Leer de un archivo de la tercera a la septima linea:")
with open("file.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for i in range(2, 7):
        print(lines[i])

print("\n================================")

print("leer el archivo y contar la cantidad de lineas que contiene (usar un contador):")
with open("file.txt", "r", encoding="utf-8") as file:
    print(len(file.readlines()))

print("\n================================")

print("leer el archivo y contar la cantidad de caracteres (usar len):")
with open("file.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(len(content))

print("\n================================")

print("leer el archivo y contar la cantidad de palabras que contienen (usar split):")
with open("file.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(len(content.split()))

print("\n================================")

print("Leer el archivo y copiar el contenido a otro, pero solo hasta la linea 5:")
with open("file.txt", "r", encoding="utf-8") as file:
    with open("file2.txt", "w", encoding="utf-8") as file2:
        for i in range(5):
            file2.write(file.readline())

        print("Copiado con exito!")

print("\n================================")

