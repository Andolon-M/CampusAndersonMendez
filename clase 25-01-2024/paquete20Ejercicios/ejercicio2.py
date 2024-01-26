print("***************************************")
print("|               bienvenido            |")
print("---------------------------------------")

salir = 0 

while salir == 0 :
    numero=int(input("ingrese un numero"))
    
    if numero == 0:
        print("el numero es 0")
    elif numero > 0:
        print("el numero es positivo")
    elif numero < 0:    
        print("el numero es negativo")
        
    salir = int(input("para salir presione un numero diferente de 0"))