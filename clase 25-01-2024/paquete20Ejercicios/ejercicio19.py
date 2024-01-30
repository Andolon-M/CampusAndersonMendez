import random

def obtener_opcion_usuario():
    while True:
        opcion = input("Elige Piedra, Papel o Tijera: ").lower()
        if opcion in ["piedra", "papel", "tijera"]:
            return opcion
        else:
            print("Por favor, elige una opción válida.")

def obtener_opcion_computadora():
    return random.choice(["piedra", "papel", "tijera"])

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        return "¡Ganaste!"
    else:
        return "¡La computadora gana!"

def jugar_piedra_papel_tijera():
    print("Bienvenido al juego Piedra, Papel o Tijera!")
    while True:
        opcion_usuario = obtener_opcion_usuario()
        opcion_computadora = obtener_opcion_computadora()
        
        print(f"Tú elegiste: {opcion_usuario}")
        print(f"La computadora eligió: {opcion_computadora}")
        
        resultado = determinar_ganador(opcion_usuario, opcion_computadora)
        print(resultado)
        
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo != "s":
            break

jugar_piedra_papel_tijera()
