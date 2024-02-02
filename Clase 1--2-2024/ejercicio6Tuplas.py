try:
    tupla = ("Tomates", "Cebollas", "Brocoli", "Papas")

    print(tupla)
    elemento = input("de que elemento desea saber su numero de pocision \n")
    print("Ese elemento esta en la pocision", tupla.index(elemento),"\n GRACIAS ************")


except ValueError:
    print("¡Ups! No se pudo hacer eso")

