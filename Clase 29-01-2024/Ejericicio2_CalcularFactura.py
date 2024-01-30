"""
Calculo de precio con descuento: Implementa una funcion que reciba dos prametros: el precio original de u producto y el porcentaje
de descuento aplicable a ese producto. La cunfion debe calcular y retornar el precio del producto despue de aplicar el descuento.
"""

def Bienvenida():
    print("***************************************")
    print("|               bienvenido            |")
    print("---------------------------------------")
    
    productos()
    
def aplicarDescuento(PrecioSinDescuento, Descuento):
    total = PrecioSinDescuento - ((PrecioSinDescuento*Descuento)/100)
    return total

def aplicarInpuesto(PrecioSinImpuesto, Inpuesto):
    total = PrecioSinImpuesto + ((PrecioSinImpuesto*Inpuesto)/100)
    return total

def productos():
    productos = [
        ["Producto 1", 100, 10, 15],
        ["Producto 2", 2000, 5, 10],
        ["Producto 3", 50, 0, 5],
    ]
    mostrarProductos(productos)
    seleccionarProduct(productos)
    return productos

def mostrarProductos(productos):
        
        for producto in productos:
            print("Nombre:", producto[0])
            print("Precio:", producto[1])
            print("Descuento:", producto[2])
            print("Impuesto:", producto[3],"\n -  -  -  - - - - - - - - - - - - - - - -") 

def seleccionarProduct(productos):
    productosAComprar = []
    while True:
        nombre_producto = input("Ingrese el nombre del producto que desea comprar: ")
        cantidad_producto = int(input("Ingrese la cantidad que desea comprar: "))
        producto_encontrado = False
        
        for producto in productos:
            if producto[0] == nombre_producto:
                productosAComprar.append((producto, cantidad_producto))
                print("El producto:", producto[0], "se agregó correctamente")
                producto_encontrado = True
                break
        
        if not producto_encontrado:
            print("El producto:", nombre_producto, "no se agregó correctamente. PUEDE QUE NO EXISTA")
            
        agregarProducto = input("¿Quiere agregar un nuevo producto? (s/n): ").lower()
        if agregarProducto != "s":
            break
    ProcesaPago(productosAComprar)
    return productosAComprar

def ProcesaPago(productosCompra):
    total = 0
    for producto, cantidad in productosCompra:
        precio_unitario = producto[1]  
        descuento= producto[2] * cantidad
        impuesto= producto[3]
        totalConDescuento= aplicarDescuento(precio_unitario, descuento)
        total= aplicarInpuesto(totalConDescuento,impuesto)
        print("total a pagar:",total)
    return total

Bienvenida()