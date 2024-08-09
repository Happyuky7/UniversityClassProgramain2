# 3 Escribir un archivo con nombres y otros con apellidos
# deben tener la misma cantidad (Minimo 4 de cada uno)

class FilesManager():

    # 3 Escribir un archivo con nombres y otros con apellidos
    # deben tener la misma cantidad (Minimo 4 de cada uno)

    def create_files(filename, fileextension, data):
        with open(f"{filename}.{fileextension}", "w", encoding="utf-8") as file:
            file.write("\n".join(data))

    # 3.1 Visualizar el archivo Completo.

    def read_file(filename, fileextension):
        with open(f"{filename}.{fileextension}", "r", encoding="utf-8") as file:
            print(file.read())

    # 3.1.1 Convbinar los archivos
    # En una linea debe estar un nombre y un apellido.
    def merge_files(filename1, filename2, fileextension):

        data1 = []
        data2 = []
        
        with open(f"{filename1}.{fileextension}", "r", encoding="utf-8") as file1:
            data1 = file1.readlines()

        with open(f"{filename2}.{fileextension}", "r", encoding="utf-8") as file2:
            data2 = file2.readlines()

        with open(f"merged.{fileextension}", "w", encoding="utf-8") as merged_file:
            
            for i in range(len(data1)):
                merged_file.write(f"{data1[i].strip()} {data2[i]}")
                if i < len(data1) - 1:
                    merged_file.write("\n")
                


# Inicializar lo que se pide en los otross puntos 3.x.
def main():

    nombresfile1 = ["Pepe", "María", "Mar", "Pablo"]

    apellidosfile1 = ["Pérez", "García", "López", "González"]

    FilesManager.create_files("nombres", "txt", nombresfile1)
    FilesManager.create_files("apellidos", "txt", apellidosfile1)

    print(" ")
    print(" Archivos creados.")
    print(" ")

    FilesManager.read_file("nombres", "txt")
    FilesManager.read_file("apellidos", "txt")

    print(" ")
    print("Archivos leídos.")
    print(" ")

    FilesManager.merge_files("nombres", "apellidos", "txt")
    FilesManager.read_file("merged", "txt")
    print(" ")
    print("Archivo de nombres y apellidos fusionado.")
    print(" ")

if __name__ == '__main__':
    main()