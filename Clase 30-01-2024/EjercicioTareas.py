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
            if not tareas:
                tareas.append(nuevaTarea)
            else:
               for i, tarea in enumerate(tareas):
                if tarea["Prioridad"] <= nuevaTarea["Prioridad"]:
                    tareas.insert(i, nuevaTarea)
                    break
                else:
                    tareas.append(nuevaTarea)
        else:
            print("Por favor, ingresa un N��MERO DE PRIORIDAD válido.")

def listarTareas():
    global tareas
    for tarea in tareas:
        print(tarea["Nombre"], tarea["Prioridad"])
    
def main():
    saludar()
    while True:
        menu()
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            crearTarea()
        elif opcion == 2:
            listarTareas()
        '''elif opcion == 3:
            modificar_tarea()
        elif opcion == 4:
            eliminar_tarea()
        elif opcion == 5:
            salir()
        else:
            print("Opcion no valida")'''
            
main()