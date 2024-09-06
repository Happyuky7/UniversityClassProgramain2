"""
Escribe programa llamado `copy_file.py` que tome dos nombres de archivo como parámetros entregados por el usuario. C
onsiderar un archivo de ‘origen’ y uno de ‘destino’. El programa debe copiar el contenido del archivo fuente al archivo de destino línea por línea

#Ejemplo: 

Ingrese el nombre de archivo origen: intro.txt 

Ingrese el nombre de archivo destino: intro_copia.txt 

Se copió el contenido de intro.txt en el nuevo archivo intro_copia.txt
"""

import shutil
import os

# Definimos la función para copiar el archivo
def copy_file(origen, destino):

    # Verificamos si el archivo origen existe y si el directorio de destino existe
    if not os.path.exists(origen):
        return print(f"El archivo {origen} no existe")
    
    # Obtenemos el path actual y los paths de origen y destino
    path = os.getcwd()
    path_origen = os.path.join(path, origen)
    # Reemplazamos los slashes "/" por los backslashes "\" en caso de ser necesario
    path_destino = os.path.join(path + "\\" + destino.replace("/", "\\"))

    # DEBUG: Comprobación de los paths
    #print(path_origen)
    #print(path_destino)
    #print(path)

    # Verificamos si el archivo destino ya existe
    if os.path.exists(path_destino):
        return print(f"El archivo {destino} ya existe")

    # Creamos el archivo destino y copiamos el contenido del archivo origen
    os.makedirs(os.path.dirname(path_destino), exist_ok=True)
    shutil.copyfile(path_origen, path_destino)

    # Enviamos un mensaje de confirmación al usuario
    return print(f"""
Se copió el contenido de 
{path_origen} 
en un nuevo archivo en 
{path_destino}
""")


# Definimos la función principal
def main():

    print("----------------------------------------")
    print("Este programa copia el contenido de un archivo origen en un archivo destino")
    print("----------------------------------------")
    print("Formas de ingresar los nombres de archivo: ")
    print("- Origen: path/intro.txt")
    print("- Destino: path/intro_copia.txt")
    print(" O ")
    print("- Origen: intro.txt")
    print("- Destino: intro_copia.txt")
    print("----------------------------------------")
    print("----------------------------------------")
    # Solicitamos al usuario que ingrese el nombre y/o path del archivo origen y destino más la extensión del archivo.
    origen = input("Ingrese el nombre de archivo origen (con extensión): ")
    print("----------------------------------------")
    destino = input("Ingrese el nombre de archivo destino (con extensión): ")
    print("----------------------------------------")

    # Llamamos a la función para copiar el archivo
    copy_file(origen, destino)


# Inicializamos el programa
if __name__ == "__main__":
    main()