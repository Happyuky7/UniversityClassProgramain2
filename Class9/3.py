# 2.2 Crear una nueva carpeta

"""
Usando el comando os.mkdir() crear una nueva carpeta de destino

- mover el archivo nombres.txt a dicha carpeta, usar libreria shutil.
"""

import os
import shutil

def create_folder(folder):
    try:
        os.mkdir(folder)
    except FileExistsError:
        print(f"La carpeta {folder} ya existe")

def move_file(file, folder):
    shutil.move(file, folder)

def main():
    
    create_folder("nombres")
    move_file("nombres.txt", "nombres")
    print("Archivo movido")

if __name__ == "__main__":
    main()
