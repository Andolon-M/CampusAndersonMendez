print("|              Bienvenido                    |")
print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  - -")

import random

horasTrabajadas = int(input("INGRESE LAS HORAS TRABAJADAS"))
categoria1=5
categoria2 = 10
categoria3 = 15
if horasTrabajadas <=10:
    totalpagar = categoria1*horasTrabajadas
    print("se le deben pagar",totalpagar,"por",horasTrabajadas,"horas trabajadas")
elif horasTrabajadas >10 and horasTrabajadas<=20:
    totalpagar = categoria2*horasTrabajadas
    print("se le deben pagar",totalpagar,"por",horasTrabajadas,"horas trabajadas")
    
elif horasTrabajadas >20:
    totalpagar = categoria3*horasTrabajadas
    print("se le deben pagar $"+totalpagar,"por",horasTrabajadas,"horas trabajadas")