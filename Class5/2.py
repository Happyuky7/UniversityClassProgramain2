# 4 Desde Pantalla
# Crea un programa que vaya leyendo las frases que el usuario teclea mediante la consola y las guarde en un fichero de texto
# llamado "registroUsuario.txt". Terminara cuando la frase introducida sea "fin" (esa frase bi deberá guardarse en el fichero).
# Luego visualizal en pantalla

def save_to_file(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(data)

def read_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()
    
filename = "registroUsuario.txt"

frases = []

while True:
    frase = input("Introduce una frase (o 'fin' para terminar): ")

    if frase.lower() == "fin":
        print("Frases guardadas correctamente en el archivo:", filename)
        print("Contenido del archivo:")
        print(read_from_file(filename))
        print()
        break
    
    frases.append(frase + "\n")

    save_to_file(filename, "".join(frases))

    
