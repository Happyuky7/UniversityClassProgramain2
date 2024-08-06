# 2.1 Crea un archivo con 3 lineas, con un mensaje que tu quieras.

with open('archivocualquiera1.txt', 'w') as file:
    for i in range(3):
        file.write(f"Linea {i+1}: Hola Mundo\n")

# 2.1.1 Ahora lee y muestra el contenido del archivo.

with open('archivocualquiera1.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line)

# 2.1.2 Ahora contamos la cantidad de lineas

with open('archivocualquiera1.txt', 'r') as file:
    lines = file.readlines()
    print(f"El archivo tiene {len(lines)} lineas.")

# 2.1.3 Ahora solo los caracteres totales

with open('archivocualquiera1.txt', 'r') as file:
    content = file.read()
    print(f"El archivo tiene {len(content)} caracteres.")

# 2.1.4 Ahora solo las palabras.

with open('archivocualquiera1.txt', 'r') as file:
    content = file.read()
    words = content.split()
    print(f"El archivo tiene {len(words)} palabras.")