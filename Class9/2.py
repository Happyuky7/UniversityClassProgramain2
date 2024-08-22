# 2.1 Crear carpetas:

"""
Usando el archivo de **nombres.txt**, crear una carpeta para cada nombre, usar try an except para
crear el nombre de la carpeta, en caso de que esta exita decir que la carpeta "ya exite".
"""

import os

def create_folder(folder):
    try:
        os.mkdir(folder)
    except FileExistsError:
        print(f"La carpeta {folder} ya existe")

with open("nombres.txt", "r", encoding="utf-8") as file:
    
    namelist = file.read().splitlines()
    print(namelist)
    
    for name in namelist:
        create_folder(name)
    
    print("Carpetas creadas")

    
    