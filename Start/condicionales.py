# CAPITULO 2: Booleanos, condicionales y entrada de usuario

# Entrada de datos. Identificacion del tipo de dato
"""
edad = input("Introduce tu edad por favor:")
tipo_de_dato = type(edad)
print(edad) """

# Booleanos. IF
verdadero = True
falso = False
if(verdadero == True):
    print("Es verdadero")
if(falso == False):
    print("Es falso")

# Operadores de comparacion. Elsif. Else
# Ejemplo portero de una discoteca
"""edad = input("Dime tu edad por favor")
# Casting a valor entero
edad = int(edad)

if(edad >= 18):
    print("Puedes entrar")
elif (edad < 14):
    print("Eres menor")
elif (edad < 0):
    print("Oye es imposible")
else:
    print("No puedes pasar. Eres menor de edad")"""

# Operadores logicos AND OR NOT
"""
# REUTILIZANDO EJEMPLO
edad = input("Dime tu edad por favor: ")
# Casting a valor entero
edad = int(edad)

if(type(edad) == int):
    if(edad > 120 or edad < 0):
        print("Esto es imposible")
    elif(edad > 18 and edad < 40):
        print("Puedes entrar al club")
    elif(edad < 18 and edad > 15):
        print("Eres muy joven todavia. No puedes entrar")
    else:
        print("No ha cumplido una condicion idonea")
else:
    print("La edad debe ser un numero entero")
"""
"""
if(not(edad <= 15)):
    print("Puedes pasar")
else:
    print("Eres menor no puedes pasar")
"""

# Ejercicio: Comprobar si el usuario introduce un numero, si no es un numero
# indicar que deber introducir un entero. Si es un numero, debemos comprar 
# si es o no par y notificarlo al usuario

numero = input("Introduce un numero:")

if(numero.isnumeric() == True):
    operacion = int(numero) % 2
    if(operacion == 0):
        print("Es un numero par")
    else: 
        print("no es un numero par")
else:
    print("No es un numero. Introduzca un numero valido")
