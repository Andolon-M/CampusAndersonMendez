adjetivo = "Asombroso"
print (adjetivo)

def mifunction():
    global adjetivo
    adjetivo = "Fantastico"
    print (adjetivo)
    #return adjetivo

mifunction()
print ("python es ", adjetivo)