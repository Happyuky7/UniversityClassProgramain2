# 8 Codigos Validos
# Crear una funcion llamada almacenar_usuario() que reciba las siguientes dos listas:
#
# nombres = ["Felipe", "Abel", "Pedro", "Juan", "Alberto", "Angella"]
# codigo = [777, 555, 755, 755, 757, 777]
#
# Cada nombre tiene un codigo asociado y tienen una relacion 1:1. La funcion debera crear dos
# archivps, uno llamado "usuariosValidos.txt" y otros "usuariosNoValidos.txt" y debera 
# almacenar en el archivo "usuariosValidos.txt" aquellos nombres cuyo codigo asociado sea 777
# y el archivo "usuariosNoValidos.txt" todos los otros nombres.

nombres = ["Felipe", "Abel", "Pedro", "Juan", "Alberto", "Angella"]
codigo = [777, 555, 755, 755, 757, 777]


def almacenar_usuarios(nombre, codigo):

    validos = []
    no_validos = []

    for i in range(len(nombre)):
        if codigo[i] == 777:
            validos.append(nombre[i])
            print(f"El usuario {nombre[i]} es valido")
        else:
            no_validos.append(nombre[i])
            print(f"El usuario {nombre[i]} es invalido")

    with open("usuariosValidos.txt", "w") as file1:
        for usuario in validos:
            file1.write(f"{usuario}\n")
        print("Se ha creado el archivo usuariosValidos.txt")
    
    with open("usuariosNoValidos.txt", "w") as file2:
        for usuario in no_validos:
            file2.write(f"{usuario}\n")
        print("Se ha creado el archivo usuariosNoValidos.txt")

almacenar_usuarios(nombres, codigo)