'''
Calculadora de Índice de Masa Corporal (IMC): Crea un programa que calcule
el IMC y clasifique el resultado en diferentes categorías de peso.
'''

print("***************************************")
print("|               bienvenido            |")
print("---------------------------------------")

salir = 0


while salir == 0 :
   peso = int(input("para calcular su Indice de masa corporal primero necesitamos su peso \n por favor ingrese su PESO: "))
   altura = float(input("ingrese su ALTURA: "))
   
   imc = peso/(altura**2)
   
   if imc < 18.5:
       print("su indice de masa corporal es de",imc,"que es de Bajo peso")
   elif imc >= 18.5 and imc < 25:
       print("su indice de masa corporal es de",imc,"que es de Normal")
   else:
       print("su indice de masa corporal es de",imc,"que es de Sobrepeso")


      
   salir = int(input("para salir presione un numero diferente de 0 "))      
