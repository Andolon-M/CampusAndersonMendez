
print("***************************************")
print("|               bienvenido            |")
print("---------------------------------------")

tamañoPiramide = int(input("Ingrese el número de la pirámide: "))
simbolo = "*"

for i in range(1, tamañoPiramide + 1, 2):
    print((simbolo * i).center(tamañoPiramide))

