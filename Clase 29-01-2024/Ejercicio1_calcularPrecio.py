'''
crear una funcion que pida nombre del usuario, cantidad de productos, precio
resultado (hola tienes que pagar 4 por la cantridad de productos)
'''
def productos():
    productos = [
        ["Shampoo", "Marca A", 250, "Limpieza profunda para cabello"],
        ["Jabón líquido", "Marca B", 150, "Fórmula suave para todo tipo de piel"],
        ["Pasta dental", "Marca C", 100, "Protección contra caries y sarro"],
        ["Desodorante", "Marca D", 180, "Frescura duradera"],
        ["Cepillo de dientes", "Marca E", 80, "Cerdas suaves para una limpieza eficaz"]
    ]
    return productos

def mostrarProductos(productos):
        for producto in productos:
            print("Nombre:", producto[0])
            print("Precio:", producto[1])
            print("Marca:", producto[2])
            print("Descripción:", producto[3],"\n -  -  -  - - - - - - - - - - - - - - - -")

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
    
    return productosAComprar

def ProcesaPago(productosCompra):
    total = 0
    for producto, cantidad in productosCompra:
        precio_unitario = producto[2]  # El precio unitario del producto está en la tercera posición de la tupla producto
        total += precio_unitario * cantidad  # Multiplica el precio unitario por la cantidad y suma al total
    return total

        
print("***************************************")
print("|               bienvenido            |")
print("--------------------------------------- \n Bienvenido a su sistema para calcular la cantidad a pagar") 

productos = productos()
mostrarProductos(productos) 
productosSeleccionados=seleccionarProduct(productos)
print(productosSeleccionados)
print("Ud debe pagar $",ProcesaPago(productosSeleccionados))





