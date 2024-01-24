print("***************************************")
print("|               bienvenido            |")
print("---------------------------------------")

nombre = input("ingrese el nombre")
numeroHorasTrabajadas = int(input("ingrese el numero Horas Trabajadas ")) 
CostoPorHora = int(input("ingrese el costo por hora ")) 
apagar=CostoPorHora*numeroHorasTrabajadas
print("Al señor",nombre,"se le debe:", apagar)