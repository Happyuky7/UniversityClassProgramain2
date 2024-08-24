"""
# 3.1 La respuesta.

El hacker desidió intervenir! para ello realizará:

- Una función que recibira los vectores de notas y remplazará todas aquellas que se encuentren bajo 39, por una nota
  aleatoria entre el 40 y el 45, la funcion entregara un archivo de texto con el nombre de la solemne.

- Para la asistencia, llevara todas las asistencias menores al 75% al 76% y entregara un archivo de texto con las nuevas
  asistencias.

"""

import random

estudiantes = ["Carlos", "Manuel","Diego","Juan","Leslie" ,"David"]
solemne_1 = [41,55,62,23,43,62]
solemne_2 = [41,51,10,15,20,69]
solemne_3 = [33,52,10,15,20,70]
asistencia = [82,62,99,82,73,65]

def replace_grades(grades, solemne):
    new_grades = []
    for grade in grades:
        if grade < 40:
            new_grades.append(random.randint(40, 45))
        else:
            new_grades.append(grade)
    with open(solemne, "w", encoding="utf-8") as file:
        for grade in new_grades:
            file.write(str(grade) + "\n")
    print(f"Archivo '{solemne}' creado con las nuevas notas.")

def replace_attendance(attendance, new_attendance): 
    new_attendance_list = []
    for attendance in attendance:
        if attendance < 75 or attendance > 76:
            new_attendance_list.append(attendance)
        else:
            new_attendance_list.append(random.randint(75, 76))
    with open(new_attendance, "w", encoding="utf-8") as file:
        for attendance in new_attendance_list:
            file.write(str(attendance) + "\n")
    print(f"Archivo '{new_attendance}' creado con las nuevas asistencias.")


def main():
    replace_grades(solemne_1, "solemne_1.txt")
    replace_grades(solemne_2, "solemne_2.txt")
    replace_grades(solemne_3, "solemne_3.txt")
    replace_attendance(asistencia, "asistencia.txt")
    print("Adiós!")

if __name__ == "__main__":
    main()