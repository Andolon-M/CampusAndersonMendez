tareas = []

def saludar():
    print("\n")
    print("===========================================")
    print("|                Bienvenido                |")
    print("|"'"¡Organiza tu caos, conquista tus tareas!"'"|")
    print(" -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")
    
def menu():
    print("\n")
    print("===========================================")
    print("|                Bienvenido                |")
    print("|"'"¡Organiza tu caos, conquista tus tareas!"'"|")
    print(" -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")
    print("| 1. Crear tarea")
    print("| 2. Listar tareas")
    print("| 3. Modificar tarea (AUN NO )")
    print("| 4. Eliminar tarea")
    print("| 5. Salir")
    print(" -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")
    

def crearTarea():
    while True:
        try:
            nombre =input(" \n Ingrese el nombre de la nueva tarea, (Para Cancelar Ingrese 0) ")
            if nombre == "0":
                break
            prioridad = int(input("ingrese la prioridad de la nueva tarea en un rango de 1 a 5 "))
        except ValueError:
            print("Por favor, ingresa un NÚMERO para la prioridad.EJEMPLO: "'"4"'"")
            pass
        
        if prioridad >= 1 and prioridad <= 5:
            nuevaTarea ={}
            nuevaTarea["Nombre"] = nombre
            nuevaTarea["Prioridad"] = prioridad
            global tareas
            tareas.append(nuevaTarea) 
        else:
            print("Por favor, ingresa un N��MERO DE PRIORIDAD válido.")

def listarTareas():
    global tareas
    tareas = sorted(tareas, key=lambda tareas: tareas["Prioridad"], reverse=True)
    print("\n")
    for tarea in tareas:
        print("Nombre",tarea["Nombre"], "Prioridad",tarea["Prioridad"])
    
def eliminarTarea():
    while True:
        try:
            nombre =input(" \n Ingrese el nombre de la tarea que desea eliminar, (Para Cancelar Ingrese 0) ")
            if nombre == "0":
                break
            for tarea in tareas:
                if tarea["Nombre"] == nombre:
                    tareas.remove(tarea)
                    print("Tarea",tarea, "elminada correctamente")
        except ValueError:
            print("Algo a salido mal, ingresa un nombre vaido para la tarea")
            pass

def Preguntar_menu():
    while True:
        menu()
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            crearTarea()
        elif opcion == 2:
            listarTareas()
        elif opcion == 3:
            print("Lo Siento aun estamos trabajando en esta funcion, PRONTO ESTARA DISPONIBLE")
        elif opcion == 4:
            eliminarTarea()
        elif opcion == 5:
            break
        else:
            print("Opcion no valida")
   
saludar()         
Preguntar_menu()