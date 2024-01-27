''''
Juego de Adivinanzas: Implementa un juego donde el usuario debe adivinar un número generado aleatoriamente,
dando pistas si su intento es demasiado alto o bajo.
'''

import random
print("***************************************")
print("|               bienvenido            |")
print("---------------------------------------")


salir = 0


while salir == 0 :
   numero = random.randint(1,100)
   numeroUsuario = 0
   contador = 0
   while numeroUsuario != numero:
       numeroUsuario = int(input("Ingrese un numero "))
       contador = contador+1
       if numeroUsuario > numero:
           print("ERROR. el numeor correcto es menor")
       elif numeroUsuario < numero:
           print("ERROR. el numero es MAYOR")
       else:
           print("FELICIDADES. Ha dijitado el numero correcto \n lo ha logrado en",contador,"intentos")
                   
      
   salir = int(input("para salir presione un numero diferente de 0 "))