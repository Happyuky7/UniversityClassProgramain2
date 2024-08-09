# 5 Separando pares e impares
# Utilice la función llamada random.randint(a,b) la cual devuelve un numero entero comprendido entre a y b (ambos inclusive),
# de forma aleatoria. Genere 100 numeros aleatorios comprendidos entre 0 y 1000 y almacenelos en una lista. Imprima por
# pantalla la lista con los 100 numeros aleatorios y luego almacene en un archivo llamado "numerosNoPares.txt" todos los
# numeros pares y los que no lo son, deberan ser almacenados en un archivo llamado "numerosPares.txt". Para utilizar la
# función random.randint(a,b) deberá importar la libreria random.

import random

def save_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        for line in range(len(data)):
            file.write(str(data[line]) + '\n')

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def sum_files_length(filename1, filename2):
    len1 = len([line for line in read_file(filename1).split('\n') if line.strip()])
    len2 = len([line for line in read_file(filename2).split('\n') if line.strip()])
    return len1 + len2

filename_pares = 'numerosPares.txt'
filename_no_pares = 'numerosNoPares.txt'

numeros = []
n_no_pares = []
n_pares = []

for i in range(100):
    numero = random.randint(0, 1000)
    numeros.append(numero)
    if numero % 2 == 0:
        n_pares.append(numero)
    else:
        n_no_pares.append(numero)

save_file(filename_pares, n_pares)
save_file(filename_no_pares, n_no_pares)



print('Numeros guardados correctamente en los archivos:', filename_pares, 'y', filename_no_pares)
print('Contenido de los archivos:')
print('Archivo', filename_pares)
print(read_file(filename_pares))
print()
print('Archivo', filename_no_pares)
print(read_file(filename_no_pares))
print()
print('Numeros generados:')
print(numeros)
print()
print('Cantidad de numeros generados:', len(numeros))
print('Cantidad de numeros en los archivos:', sum_files_length(filename_pares, filename_no_pares))
print()
