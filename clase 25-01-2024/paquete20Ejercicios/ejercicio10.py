'''
Sistema de Calificaciones: Escribe un programa que convierta
una puntuación numérica a una calificación alfabética
(A, B, C, etc.).
'''


print("***************************************")
print("|               bienvenido            |")
print("---------------------------------------")


salir = 0


while salir == 0 :
   nota = float(input("ingrese una nota "))
   if nota >= 0 and nota < 1:
       print("la nota ingresada se clasifica en F de Faltal")
   elif nota >= 1 and nota < 2.5:
       print("la n1ota ingresada se clasifica en D de deficiente")
   elif nota >= 2.5 and nota < 3.5:
           print("la nota ingresada se clasifica en B de Basica")
   elif nota >= 3.5 and nota < 4:
       print("la nota ingresada se clasifica en A de Aceptable")
   elif nota >= 4 and nota <= 5:
       print("la nota ingresada se clasifica en S de Sobresaliente")

      
   salir = int(input("para salir presione un numero diferente de 0 "))      
