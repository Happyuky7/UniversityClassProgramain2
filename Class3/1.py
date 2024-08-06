# Imprimir Hello World

print("Hello, World!")

# Imprimir la secuencia del 1 al 5 de numeros.

secuencia = range(1, 6)

for numero in secuencia:
    print(numero)
    if numero == 5:
        break

# Imprimir la logintud

logitud = len([1, 2, 3, 4, 5])
print(f"La secuencia tiene {logitud} elementos.")

# Devuelve el valor maximo o minimo de una secuencia

maximo = max([3, 8, 1, 5])
minimo = min([3, 8, 1, 5])

print(f"El valor maximo {maximo} elementos.")

print(f"El valor minimo {minimo} elementos.")

# ordena elementos de una secuencia

lista_ordenada = sorted([5, 2, 8, 1, 3])

print(f"La secuencia ordenada {lista_ordenada}.")