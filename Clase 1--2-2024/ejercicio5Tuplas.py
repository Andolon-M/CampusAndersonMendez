try:
    tupla = ("Tomates", "Cebollas", "Brocoli", "Papas")

    print(tupla)
    inicio = int(input("desde que pocision quiere ver la tupla \n"))
    print(tupla[inicio:])


except ValueError:
    print("¡Ups! No se pudo hacer eso")
