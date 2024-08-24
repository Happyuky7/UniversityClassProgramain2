"""
# 3 El Riesgo!

# 3.1

Los mismos alumnos del ejercicio de aprobación:

estudiantes = ["Carlos", "Manuel","Diego","Juan","Leslie" ,"David"]
solemne_1 = [41,55,62,23,43,62]
solemne_2 = [41,51,10,15,20,69]
solemne_3 = [33,52,10,15,20,70]
asistencia = [82,62,99,82,73,65]

Decidieron contratar un hacker, para aprobar el curso, más este puso sus condiciones:

- Los alumnos deben pagarle 100 USD, por cada vocal que contenga su nombre
- Requiere que le envien los valores que pagaran en un archivo llamado "soborno.txt"

"""

estudiantes = ["Carlos", "Manuel","Diego","Juan","Leslie" ,"David"]
solemne_1 = [41,55,62,23,43,62]
solemne_2 = [41,51,10,15,20,69]
solemne_3 = [33,52,10,15,20,70]
asistencia = [82,62,99,82,73,65]

def count_vowels(name):
    vowels = "aeiouAEIOUáéíóú"
    return sum(1 for char in name if char in vowels)

def calculate_total_amount(student_names):
    total = 0
    for name in student_names:
        total += count_vowels(name) * 100
        print(f"El alumno {name} pagará: {count_vowels(name) * 100} USD")
    return total

def write_to_file(total_amount, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(str(total_amount))
        print(f"El monto total a pagar es: {total_amount} USD")

def main():
    total_amount = calculate_total_amount(estudiantes)
    file_path = "soborno.txt"
    write_to_file(total_amount, file_path)
    print(f"Archivo '{file_path}' creado con el monto total a pagar.")
    print("Adiós!")

if __name__ == "__main__":
    main()