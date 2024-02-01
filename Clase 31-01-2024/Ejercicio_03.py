#se crea la funcion para hacer covertir numeros pares en impares y numeros pares en impares
def incremParesEimpares(listaNumeros): 
   #lista interna que almacenara los nuevos numeros modificados
    paresYPrimosInvertidos = []  
    # ciclo para recorrer la ista recibida 
    for numero in listaNumeros: 
        # si el recidio al dividir ente 2 es cero significa que el numero en esa posicion de la lista es par.
        if numero % 2 == 0: 
          paresYPrimosInvertidos.append(numero - 1) #se resta -1 para hacer el numero inpar.
        #de lo contrario.
        else:
            paresYPrimosInvertidos.append(numero + 1) # se suma 1 al numero para hacerlo par.
    #retornamos la nueva lista segun los solicitado.
    return paresYPrimosInvertidos

#seccion principal del programa.
print("\n Bienvenido") #mensaje de bienvenida
listaNumero = [] # variable tipo lista que almacenara los numeros ingresados

#se iiia un bucle de tipo while para solicitar un numero hasta que el usuario ingrese el numero -999
while True:
    #se usa un bloque de codigo try para manejar de mejor manera el caso de que el usuario ingrese algo diferente a un numero.
    try: 
        numero = int(input("Ingresa un número (-999 para terminar): "))
        if numero == -999:
            #dejamos de solicitar un numero si el usuario ingresa -999
            break 
             #se ingresa el numero a la lista.
        listaNumero.append(numero)
    #en caso de que se genere un error en el cloque de codigo anterior se ejecutara los siguiente.
    except ValueError:
        print("Por favor, ingresa un número válido.")

#se crea la nueva lista que sera llenada con la funcion.   
nuevaLista = incremParesEimpares(listaNumero) #a l funcion le enviamos la lista de numeros que ingreso el usuario

#mostramos la lista que nos genero la funcion.
print("la lista con los numero pares e impares invertidos es:")
for numero in nuevaLista:
    print(numero, end=', ')

#mostramos la lista origial que igreso el usaurio   
print("\nla lisa Original es:")
for numero in listaNumero:
    print(numero, end=', ')



################################################################
#finalizamos el programa...