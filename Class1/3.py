
saludo = "Hola"
nombre = "Mundo"
mensaje = saludo + " " + nombre

# Print the first letter in "mensaje"
first_letter = str(mensaje[0])
print(first_letter)

#El corte entre la segunda letra y el quinto elemento
corte_letter_5 = mensaje[1:6]
print(corte_letter_5)

# solo minusculas
print(mensaje.lower())

# solo mayuscula
print(mensaje.upper())

# replace
print(mensaje.replace('Mundo', 'Python'))