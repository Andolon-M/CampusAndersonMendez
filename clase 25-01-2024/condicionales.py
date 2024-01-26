import random
#numero=int(input("ingrese un numero"))

numero= random.randint(0,100)

if numero == 0:
    print("el numero es 0")
elif numero <0:
    print("numero es menor que cero")
    
elif  numero > 0:
    print("el numero es mayor a cero")
    