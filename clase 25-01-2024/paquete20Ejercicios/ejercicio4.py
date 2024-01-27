'''
Calculadora de Impuestos: Haz un programa que calcule el impuesto aplicado a un ingreso ingresado,
donde el impuesto varía según diferentes rangos de ingresos.
'''

print("***************************************")
print("|               bienvenido            |")
print("---------------------------------------")

salir = 0 

while salir == 0 :
    totalPagaras = 0
    precio=int(input("ingrese el presio de la compra para calcular el impuesto"))
    
    if precio == 0:
        print("el precio no puede ser 0")
        continue
    elif precio >= 100 and precio <200:
        impuesto = round(precio * 0.05)
        totalPagaras = precio + impuesto
        print("el precio de la compra es de", precio, "y el impuesto es del 5% que equivale a:", impuesto,"\n total A pagar", totalPagaras)
    elif precio >= 200 and precio <300:
        impuesto = round(precio * 0.08)
        totalPagaras = precio + impuesto
        print("el precio de la compra es de", precio, "y el impuesto es del 8% que equivale a:", impuesto,"\n total A pagar", totalPagaras)
    elif precio >= 300 and precio <400:
        impuesto = round(precio * 0.1)
        totalPagaras = precio + impuesto
        print("el precio de la compra es de", precio, "y el impuesto es del 10% que equivale a:", impuesto,"\n total A pagar", totalPagaras)
    elif precio >= 400:
        impuesto = round(precio * 0.12)
        totalPagaras = precio + impuesto
        print("el precio de la compra es de", precio, "y el impuesto es del 12% que equivale a:", impuesto,"\n total A pagar", totalPagaras)
        
    else:
        impuesto = 0
        print("el precio de la compra es de", precio, "y el impuesto es del 0% que equivale a:", impuesto)
        
        
    salir = int(input("para salir presione un numero diferente de 0"))