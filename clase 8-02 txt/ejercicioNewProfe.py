'''
Una empresa está organizando la agenda de eventos para el mes de agosto. Por lo tanto requiere un programa que:

-Permita registrar a los participantes de los eventos de agosto pidiendo: documento, nombre, edad y cargo.
-Permita registrar los eventos  pidiendo: nombre del evento, locación y día del mes
-Permita quitar del registro a los participantes .
-Permita eliminar y/o modificar eventos.

Para participar los empleados deben cancelar un aporte de 50.000 COP. Por lo tanto el programa también debe:

-Saber cuantos empleados no han cancelado aún el aporte y cuanto dinero suma la deuda.
-Saber cuales empleados (listarlos) no han cancelado.
-No permitir quitar del registro a participantes que ya hayan pagado, pues no se aceptan devoluciones
-Marcar eventos ya realizados.
-No permitir eliminar o modificar eventos ya realizados.

Aspectos a tener en cuenta: 

-La estructura a utilizar es libre, solo se pide que sea ordenada y coherente. 
-Todo debe ser dentro de un menú que se repite para no perder la información y al presionar la opción de salida se debe pedir confirmación de la misma. 
-Se deben manejar la excepciones
'''

#en la lista empleados se guardara un diccionario cuya clave sera el documento de cada empleado, cuyo valor sera una
#tupla que contendra la informacion del usuario
empleados = []
eventos = []
aPagado = []
deben   = []
costoEventos = 50.000

def añadir(documento, nombre, edad, cargo):
    global empleados
    dataEmpleado=(nombre, edad, cargo)
    empleado = {documento: dataEmpleado}
    empleados.append(empleado)
    
def solicitarInformacion():
    documento = int(input("\nIngrese el documento del empleado: "))
    nombre = input("Ingrese el nombre del empleado: ")
    edad = int(input("Ingrese la edad del empleado: "))
    cargo = input("Ingrese el cargo del empleado: ")
    añadir(documento, nombre, edad, cargo)
    
def añadirEvento(nombre, locacion, diaMes):
    global eventos
    dataEvento = (nombre, locacion, diaMes)
    if not eventos:
        #si no hay eventos creados
       evento = {1: dataEvento}
       eventos.append(evento)
    else:
        #si hay eventos creados
        evento = {len(eventos)+1: dataEvento}
        eventos.append(evento)
        
def solicitarInformacionEvento():
    nombre = input("Ingrese el nombre del evento: ")
    locacion = input("Ingrese la locación del evento: ")
    diaMes = int(input("Ingrese el día del mes: "))
    añadirEvento(nombre, locacion, diaMes)
    
def añadirPagado(costo):
    global aPagado, deben, empleados    
    print("El evento tiene un costo de $", costo )
    documento = int(input("Ingrese el documento del empleado que desea pagar: "))
    for empleado in empleados:
        if documento in empleado:
            aPagado.append(empleado)
            print("El empleado", documento, "ha sido pagado correctamente")
            break
        else:
            print("El empleado", documento, "no se encontro. no se hizo ningun pago.")
   
def verificarPagos():
     for empleado in empleados:
        if empleado not in aPagado:
            deben.append(empleado)
            break
       
def mostrarEventos():
    global eventos
    for evento in eventos:
        print(evento)
        
def mostrarEmpleados():
    global empleados
    for empleado in empleados:
        print(empleado)
        
def eliminarEmpleado():
    global empleados
    documento = int(input("Ingrese el documento del empleado que desea eliminar: "))
    for empleado in empleados:
        if documento in empleado:
            empleados.remove(empleado)
            print("El empleado", documento, "ha sido eliminado correctamente")
            break
        else:
            print("El empleado", documento, "no se ha eliminado correctamente")
            
def elinarEvento():
    global eventos
    numero = int(input("Ingrese el numero del evento que desea eliminar: "))
    for evento in eventos:
        if numero in evento:
            eventos.remove(evento)
            print("El evento", numero, "ha sido eliminado correctamente")
            break
        else:
            print("El evento", numero, "no se ha eliminado correctamente")
          
def listarPagos():
    global aPagado
    for empleado in aPagado:
        print(empleado)
  
def menu():
    while True:
        print("1. Registrar empleado")
        print("2. Registrar evento")
        print("3. Mostrar eventos")
        print("4. Mostrar empleados")
        print("5. Eliminar empleado")
        print("6. Eliminar evento")
        print("7. Añadir el pago de un asistente")
        print("8. Listar asistentes que han pagado")
        print("0. Salir")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            solicitarInformacion()
        elif opcion == 2:
            solicitarInformacionEvento()
        elif opcion == 3:
            mostrarEventos()
        elif opcion == 4:
            mostrarEmpleados()
        elif opcion == 5:
            eliminarEmpleado()
        elif opcion == 6:
            elinarEvento()
        elif opcion == 7:
            añadirPagado(costoEventos)
            verificarPagos()
        elif opcion == 8:
            mostrarEmpleados()
        elif opcion == 0:
            break
        else:
            print("Opción incorrecta")

    
menu()
