'''
Clasificador de Palabras: Escribe un programa que clasifique una palabra ingresada como 'corta'
(menos de 5 caracteres), 'media' (entre 5 y 10 caracteres) o 'larga' (más de 10 caracteres).
'''

print("***************************************")
print("|               bienvenido            |")
print("---------------------------------------")

salir = 0 

while salir == 0 :
    
    palabra = input("ingrese una palabra para verificar su categoria")
    
    if len(palabra) < 5:  
        print("la palabra", palabra, "es corta")
    elif len(palabra) >= 5 and len(palabra) <= 10:
        print("la palabra", palabra, "es media")
    elif len(palabra) > 10:
        print("la palabra", palabra, "es larga")
    
    salir = int(input("para salir presione un numero diferente de 0"))