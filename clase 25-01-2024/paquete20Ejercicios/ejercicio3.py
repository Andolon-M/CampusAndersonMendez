'''Detector de Año Bisiesto: Escribe un script que 
determine si un año ingresado es bisiesto o no.'''

print("***************************************")
print("|               bienvenido            |")
print("---------------------------------------")

salir = 0 

while salir == 0 :
    año = 0
    año=int(input("ingrese un año para saber si es bisiesto"))
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                print("El año", año, "es bisiesto")
            else:
                print("El año", año, "no es bisiesto")
        else:
            print("El año", año, "es bisiesto")
    else:
        print("El año", año, "no es bisiesto")

   
        
    salir = int(input("para salir presione un numero diferente de 0"))