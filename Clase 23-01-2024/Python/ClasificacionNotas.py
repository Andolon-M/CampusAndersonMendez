print("***************************************")
print("|               bienvenido            |")
print("---------------------------------------")
salir = 1
while salir != 0:
    
    nota = int(input("ingrese una nota para verificar su Categoria"))
    if nota >= 0 and nota <= 2.2:
        print("la nota ingresada es D de DESEPCIONANTE")
    elif nota >= 2.3 and nota <= 2.9:  
        print("la nota ingresada es C")
    elif nota >= 3.0 and nota <= 3.8:  
        print("la nota ingresada es B de BASICA")
    elif nota >= 3.9 and nota<= 5:  
        print("la nota ingresada es A de ACEPTABLE")
        
    else:
     print ("esa nota no esta en el rango calificable")
     
     
        
    salir = int(input("desea continuar en el programa? \n PRESIONE \n 1. PARA NO \n 0 para SI"))
    
    '''
    hola
    '''
