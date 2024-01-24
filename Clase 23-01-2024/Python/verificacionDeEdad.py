print("***************************************")
print("|               bienvenido            |")
print("---------------------------------------")
salir = 1
while salir != 0:
    edad=int(input("\nVamos a verificar su edad\nINGRESE SU EDAD"))
    if edad >= 18:
        print("si puede votar porque su edad es:",edad)
    else:
        print("no puede votar porque su edad es:",edad,"y debe se mayor de 18")
    salir = int(input("desea continuar en el programa? \n PRESIONE \n 1. PARA NO \n 0 para SI"))
