try:
    tupla = ("Tomates", "Cebollas", "Brocoli", "Papas")

    print(tupla)
    aModificar = input("¿Qué elemento desea modificar?\n")

    lista = list(tupla)

    for indice, elemento in enumerate(lista):
        if elemento == aModificar:
            menu = int(input("¿Qué desea hacer con este elemento?\n 1. Cambiar el nombre\n 2. Eliminar\n"))
            if menu == 1:
                nuevoNombre = input("Ingrese el nuevo nombre:\n")
                lista[indice] = nuevoNombre
            elif menu == 2:
                lista.remove(elemento)

    tupla_modificada = tuple(lista)
    print("Tupla modificada:", tupla_modificada)

except ValueError:
    print("¡Ups! No se pudo hacer eso")
