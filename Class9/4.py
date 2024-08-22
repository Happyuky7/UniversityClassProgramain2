"""
A partir de las siguientes listas (relación1:1):

estudiantes = ["Carlos", "Manuel","Diego","Juan","Leslie" ,"David"]
solemne_1 = [41,55,62,23,43,62]
solemne_2 = [41,51,10,15,20,69]
solemne_3 = [33,52,10,15,20,70]
asistencia = [82,62,99,82,73,65]


Escriba las siguientes funciones:

estadoEstudiante(nombre): Función que recibe un nombre de estudlante como varlable de entrada y retoma un 1 siel
estudiante aprobó, un 2 si el estudiante no aprobo y un 3 si el estudiante no se encuentra en la lista. Consldere que para
que un alumno apruebe, el promedio de sus 3 notas es mayor o igual a 40 y su asistencia es igual o superior a 75.

aprobadosReprobados(nombre): Función que recibe un nombre d e estudiante como variable de entrada. Esta función
deberá almacenar en un archivo al estudiante ingresado según los siguientes criterios: Sl el estudiante aprobo, deberá
ser almacenado en un fichero lamado "aprobados.cxl". * - S i el estudiante reprobó, deberá ser almacenado en un fichero
llamado "reprobados.txt".*- Si el estudiante no se encuentra en la lista, la función deberá imprimir por pantalla el
siguiente mensaje: "El estudiante no se puede registrar, ya que no se encuentra en la lista
"""


import os
import shutil

estudiantes = ["Carlos","Manuel","Diego","Juan","Leslie","David"]
solemne_1 = [41,55,62,23,43,62]
solemne_2 = [41,51,10,15,20,69]
solemne_3 = [33,52,10,15,20,70]
asistencia = [82,62,99,82,73,65]

def calcular_promedio(notas):
    suma_notas = 0
    for i in range(len(notas)):
        suma_notas += notas[i]
    return suma_notas / len(notas)
        

def status_studying(name : str):
    
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

if __name__ == "__main__":
    main()
    

    