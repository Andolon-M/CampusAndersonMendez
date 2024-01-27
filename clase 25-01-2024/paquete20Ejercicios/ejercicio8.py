print("***************************************")
print("|               bienvenido            |")
print("---------------------------------------")

salir = 0 

while salir == 0 :
    lista = []

    # Solicitar al usuario que ingrese los números
    while True:
        try:
            numero = int(input("Ingresa un número (-999 para terminar): "))
            if numero == -999:
                break
            lista.append(numero)
        except ValueError:
            print("Por favor, ingresa un número válido.")

    # Ordenar la lista
    lista.sort()

    # Mover números negativos al inicio
    lista_negativos = [num for num in lista if num < 0]
    lista_sin_negativos = [num for num in lista if num >= 0]
    lista = lista_negativos + lista_sin_negativos

    # Imprimir la lista ordenada
    print("Lista ordenada:", lista)

    salir = int(input("Para salir, presione un número diferente de 0: "))
