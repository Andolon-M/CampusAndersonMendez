print("|              Bienvenido                    |")
print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  - -")
descurnto1 = 15
descurnto2 = 10
totalPagar = 0
costoUnidad = 500
docena= 12
productosCompra= int(input("cuantos productos desea comprar "))
totalPagar = productosCompra*costoUnidad
if productosCompra > docena*3:
    print("usted esta comprando ",productosCompra//docena, "docenas")
    print("Valor neto sin desceuentos $",totalPagar )
    descuento = ((totalPagar/100)*descurnto1)
    print("Su descuento es de : $",descuento)
    totalPagar = totalPagar - descuento
    print("ud esta comprado mas de tres docenas, por lo tanto su descuento es de",descurnto1,"% \n El total A pagar es $",totalPagar)
    prodectosObsequi=(productosCompra//(docena)-3)
    print("productos obsequiados: ",prodectosObsequi)
else:   
    totalPagar = totalPagar-((totalPagar/100)*descurnto2)
    print("ud esta comprado mas de tres docenas, por lo tanto su descuento es de",descurnto1,"% \n El total A pagar es $",totalPagar)