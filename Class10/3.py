"""
#3.1 El todo por el todo!

El hacker remplazará todos los archivos modificados de la carpeta del profesor llamada "carpeta_profesor", que contienen
los archivos de texto originales, por los que modifico, para ello usará "os" y "shutil" de la siguiente forma.

- Ingresará a la "carpeta_profesor" usando os
- Eliminará los archivos que modificará
- Usará shutil, para mover sus archivos modificados a la carpeta mencionada.
- Finalmente usando el codigo de clases, generara el archivo "aprobados.txt", con los nuevos resultados.
"""

import os
import shutil

def create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Carpeta '{folder}' creada!")
    else:
        print(f"Carpeta '{folder}' ya existe!")

def join_path(folder):
    return os.path.join(os.getcwd(), folder)

def remove_files(folder, files):
    for file in files:
        if os.path.exists(os.path.join(folder, file)):
            os.remove(os.path.join(folder, file))
            print(f"Archivo '{file}' eliminado!")
        else:
            print(f"Archivo '{file}' no existe!")


def move_files(folder_from, folder_to, files):
    for file in files:
        if os.path.exists(os.path.join(folder_from, file)):
            
            if os.path.exists(os.path.join(folder_to, file)):
                print(f"Archivo '{file}' ya existe en '{folder_to}'!")
                continue
            else:
                shutil.move(os.path.join(folder_from, file), os.path.join(folder_to, file))
                print(f"Archivo '{file}' movido de '{folder_from}' a '{folder_to}'!")
                
            
        else:
            print(f"Archivo '{file}' no existe!")


def create_file(folder, file, data):
    with open(os.path.join(folder, file), "w", encoding="utf-8") as file:
        for item in data:
            file.write(str(item) + "\n")
    print(f"Archivo '{file}' creado!")



def calcular_promedio(notas):
    suma_notas = 0
    for i in range(len(notas)):
        suma_notas += notas[i]
    return suma_notas / len(notas)
        

estudiantes = ["Carlos","Manuel","Diego","Juan","Leslie","David"]

def status_studying(name : str):
    
    solemne_1 = []
    solemne_2 = []
    solemne_3 = []

    with open("solemne_1.txt", "r", encoding="utf-8") as file:
        for line in file:
            solemne_1.append(int(line))
    
    with open("solemne_2.txt", "r", encoding="utf-8") as file:
        for line in file:
            solemne_2.append(int(line))

    with open("solemne_3.txt", "r", encoding="utf-8") as file:
        for line in file:
            solemne_3.append(int(line))

            
    if name in estudiantes:
        for stu in range(len(estudiantes)):
            print(estudiantes[stu])
            if (name == estudiantes[stu]):
                print(f"EL estudiante exite en la lista ({name})")
                
                sol1 = solemne_1[stu]
                sol2 = solemne_2[stu]
                sol3 = solemne_3[stu]
                
                notas = [sol1,sol2,sol3]
                
                print(f"len notAs: {len(notas)}")
                
                promedio = calcular_promedio(notas)
                
                print(f"Promedio: {promedio}")
                
                if (promedio >= 40):
                    return 1
                else:
                    return 2
            
    else:
        print(f"EL estudiante NO exite en la lista ({name})")
        return 3
        
def aprobadosReprobados(name : str):

    print(f"Estudiante: {name}")
    
    status = status_studying(name)
    
    if status == 1:
        with open("aprobados.txt", "a", encoding="utf-8") as file:
            file.write(name + "\n")
            print(f"El estudiante {name} ha sido registrado en aprobados")
    elif status == 2:
        with open("reprobados.txt", "a", encoding="utf-8") as file:
            file.write(name + "\n")
            print(f"El estudiante {name} ha sido registrado en reprobados")
    else:
        print("El estudiante no se puede registrar, ya que no se encuentra en la lista")


def main():
    aprobadosReprobados("Carlos")
    aprobadosReprobados("Manuel")
    aprobadosReprobados("Diego")
    aprobadosReprobados("Juan")
    aprobadosReprobados("Leslie")
    aprobadosReprobados("David")
    aprobadosReprobados("Fernando")

    folder_profesor = "carpeta_profesor"
    files_to_remove = ["aprobados.txt", "reprobados.txt"]

    remove_files(folder_profesor, files_to_remove)
    files_to_move = ["aprobados.txt", "reprobados.txt"]
    move_files(os.getcwd(), join_path(folder_profesor), files_to_move)
    

    #remove_files(files_to_remove)

if __name__ == "__main__":
    main()