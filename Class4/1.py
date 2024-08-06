msg1 = """lorem_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

with open("test.txt", "w") as file:
    file.write(lorem_text)"""

with open("archive2.txt", "w") as archive:
    archive.write(msg1)
    print("Archivo Creado: " + archive.name)

with open("archive2.txt", "r") as archive:
    print(archive.read())
    print("Total de lineas en el archivo: " + str(len(archive.readlines())))

with open("archive2.txt", "r") as archive:
    lines = archive.readlines()
    for i in range(len(lines)):
        print(f"Linea: {i+1}: {lines[i]}")