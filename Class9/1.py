import os

# 1.1 Donde estamos?

directory_actual = os.getcwd()
print(f"Directorio actual: {directory_actual}")

# 1.2 Que hay en la carpeta?

list_dir = os.listdir()
print(f"{list_dir}")

# 1.3 Buscar un archivo

directory = os.getcwd()
search = '.txt'

for i in os.listdir(directory):
    if i.endswith(search):
        print(i)
    else:
        print(f"No hay archivos con la(s) extencion(es): {search}")
        
        