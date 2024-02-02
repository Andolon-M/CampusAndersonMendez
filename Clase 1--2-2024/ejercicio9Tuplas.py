# Crear una tupla de tuplas
tupla_anidada = (("a", "b", "c"), (1, 2, 3), ("x", "y", "z"))

# Acceder a elementos anidados
primer_elemento = tupla_anidada[0]  # Accede a la primera tupla dentro de la tupla principal
segundo_elemento = tupla_anidada[1]  # Accede a la segunda tupla dentro de la tupla principal
tercer_elemento = tupla_anidada[2]  # Accede a la tercera tupla dentro de la tupla principal

# Acceder a elementos individuales dentro de las tuplas internas
primer_elemento_anidado = primer_elemento[0]  # Accede al primer elemento de la primera tupla
segundo_elemento_anidado = segundo_elemento[1]  # Accede al segundo elemento de la segunda tupla
tercer_elemento_anidado = tercer_elemento[2]  # Accede al tercer elemento de la tercera tupla

# Imprimir los resultados
print("Primer elemento anidado:", primer_elemento_anidado)
print("Segundo elemento anidado:", segundo_elemento_anidado)
print("Tercer elemento anidado:", tercer_elemento_anidado)
