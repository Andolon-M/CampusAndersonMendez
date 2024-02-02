try:
    tupla = ("Tomates", "Cebollas", "Brocoli", "Papas", "Brocolis", "Tomates", "Tomates")

    print(tupla)
    elemento = input("que elemento desea contar \n")
    print("Ese elemento aparece", tupla.count(elemento)," veces. \n GRACIAS ************")


except ValueError:
    print("¡Ups! No se pudo hacer eso")

