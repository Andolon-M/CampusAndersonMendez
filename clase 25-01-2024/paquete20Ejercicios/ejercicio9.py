print("***************************************")
print("|               bienvenido            |")
print("---------------------------------------")
salir = 0 
while salir == 0 :
    palidromo = input("ingrese una palabra para ver si es palidromo")

    if palidromo == palidromo[::-1]:
            print("la palabra es palidromo")
    elif palidromo == palidromo:
            print("la palabra no es palidromo")
    
salir = int(input("para salir presione un numero diferente de 0"))
