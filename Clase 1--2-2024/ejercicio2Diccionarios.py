try:
    personas_edades = {
        "Fulano": 12,
        "Mengano": 25,
        "Perengano": 30
    }

    print("El diccionario completo tiene:\n",personas_edades,)
    claveBuscar=input("\n igrese la clave que desea consultar\n")

    print("esa clave contiene \n", personas_edades[claveBuscar])

except ValueError:
    print("la clave no existe")