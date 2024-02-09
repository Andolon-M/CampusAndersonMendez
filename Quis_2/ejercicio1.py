def saludo():
    print("***************************************")
    print("|               bienvenido            |")
    print("---------------------------------------")
    
def menu():
    print("\n 1) Añadir platos al pedido\n 2) Mostrar el pedido actual\n 3) Elimminar un plato del pedido\n 4) SALIR\n ")
    desicion=int(input("INGRESE EL NÚMERO DE LA OPCION SELECCIONADA\n"))
    return desicion

def añadir(pedidos):
    try:
        if not pedidos:
            print("no hay platos, agrege el primero")
            pedido = []
            nombre = input("Ingrese el nombre del plato\n")
            cantidad = input("Ingree la cantidad del plato\n")
            plato = {nombre: cantidad}
            pedidos.append(plato)
        else:         
            nombre = input("Ingrese el nombre del plato\n")
            cantidad = input("Ingree la cantidad del plato\n")
            plato = {nombre: cantidad}
            pedidos.append(plato)
        return pedidos
    except ValueError:
        print("Ingreso un valor no valido")
        
    
def eliminarPlato(pedidos):
    print("Actualmente hay", len(pedidos), "platos en el pedido.")

    if not pedidos:
        print("No hay platos en el pedido para eliminar.")
        return

    pedidoEliminar = input("Ingrese el nombre del plato que desea eliminar: ")

    for pedido in pedidos:
        if pedidoEliminar in pedido:
            pedidos.remove(pedido)
            print(f"El plato '{pedidoEliminar}' ha sido eliminado del pedido.")
            return

    print(f"El plato '{pedidoEliminar}' no fue encontrado en el pedido.")


    
pedidos=[]
desicion = 0
while desicion != 4:
    try:
        desicion = menu()
        if desicion == 1: 
            añadir(pedidos)
           
        elif desicion == 2:
            print("Actualmente se han pedido:\n")
            contador = 1
            for pedido in pedidos:
                
                print("plato numero:", contador,") ", pedido)
                contador += 1
                desicion = 0
    
        elif desicion == 3:
            eliminarPlato(pedidos)
            
    except ValueError:
        print("UY! ALGO NO HA SALIDO BIEN")