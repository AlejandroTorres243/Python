# Capitulo 10 : Funciones - Parte 2 : Argumentos arbitrarios y keyword arguments

# Apartado 1: Argumento arbitrario
# Los argumentos arbitrarios se utilizan cuando no sabemos
# de forma exacta el numero de parametros que la funcion va a recibir
"""
def maximo(*args):
    maximo = args[0]
    for numero in args[1:]:
        if numero > maximo:
            maximo = numero
    return maximo

print(maximo(10,20,30,25,95,-110, 22.3, 1.5))
print(maximo(1,2,3,4))

def maximo2(listNumeros):
    maximo = listNumeros[0]
    for numero in listNumeros[1:]:
        if(numero > maximo):
            maximo = numero
    return maximo

print(maximo2([10,20,30,25,98,-110, 22.3, 9.3]))
"""
"""
def formatoDescarga(tipo, *args):
    numArgs = len(args)
    if(tipo == "video"):
        if(numArgs == 0):
            print(f"El formato seleccionado : \n-Tipo de archivo: {tipo}")
        elif(numArgs == 1):
            print(f"El formato seleccionado : \n-Tipo de archivo: {tipo}\n-Resolucion {args[0]}")
        elif(numArgs == 2):
            print(f"El formato seleccionado : \n-Tipo de archivo: {tipo}\n-Resolucion {args[0]} \n-FPS: {args[1]}")
    elif(tipo == "audio"):
        print(f"el formato seleccionado: \n-Tipo : {tipo}")
    else:
        print("el formato el incorrecto")

formatoDescarga("video", 720)
formatoDescarga("video", 1080, 60)
formatoDescarga("audio")
"""
# Apartado 2 : Keyword Arguments

# Podemos pasar los argumentos de una funcion
# mediante keywords. De esta forma conseguimos
# que el orden de los argumentos se indiferente
"""
def crearPersonaje(clase, raza, nombre):
    print(f"{nombre.upper()} es un {clase} de raza {raza}")

crearPersonaje(nombre="Leonidas",clase="guerrero", raza="humano")
crearPersonaje("mago", "elfo", "mandalorian")
"""
# Apartado 3 : Keyword Arbitrary Arguments

# Se utiliza cuando no sabemos cuantos argumentos de palabras
# clave vamos a recibir.
# Detalle observar como si fuera un diccionario
"""
def printKwargs(**kwargs):
    print("\n")
    print("Los atributos del personaje son: ")
    for clave, valor in kwargs.items():
        print(f"{clave} ----> {valor}")

printKwargs(nombre="Leonidas",clase="guerrero", raza="humano", mascota="Dragon", clan="Espartanos")
printKwargs(raza="mago", clase="elfo", nombre="mandalorian")
"""
# Apartado 4: Combinacion de todos los anteriores.
# Se pueden usar conjuntamente en una misma funcion

def crearPersonaje(nombre, *args, **kwargs):
    descripcion = f"####{nombre.upper()}##### \n\n"
    descripcion += '##### DESCRIPCION ####### \n\n'
    for clave, valor in kwargs.items():
        descripcion += f"- {clave} ----> {valor}\n\n"
    descripcion += "##### HABILIDADES ###### \n\n"
    for skill in args:
        descripcion += f"- {skill}\n"
    return descripcion

personaje = crearPersonaje("Dandelion", "ataque fuerte", "bola de fuego", "salto doble", "cascada", clase="mago", raza="Muerto Viviente", mascota="serpiente")
print(personaje)