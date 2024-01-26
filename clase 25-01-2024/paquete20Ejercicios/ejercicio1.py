def contiene_numero(cadena):
    for caracter in cadena:
        if caracter.isdigit():
            return True
    return False

print("***************************************")
print("|               bienvenido            |")
print("---------------------------------------")

esAceptable = False
contraseña = ""
while not esAceptable:
    contraseña = input("Ingrese una contraseña: ")
    if len(contraseña) >= 8:
        if not contiene_numero(contraseña):
            print("La contraseña debe contener al menos un número.")
        elif contraseña.islower():
            print("La contraseña contiene solo caracteres en minúscula. Agregue al menos un carácter en MAYÚSCULA.")
        elif contraseña.isupper():
            print("La contraseña contiene solo caracteres en mayúscula. Agregue al menos un carácter en minúscula.")
        else:
            print("La contraseña cumple con todos los requisitos.")
            esAceptable = True
    else:
        print("La contraseña debe ser mayor a 8 caracteres.")

