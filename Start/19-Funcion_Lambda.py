# Funcion Lambda
# Son funciones anonimas (que no tienen nombre) :
# - Permiten multiples argumentos
# - Solo puede tener una exprecion
# - Estructura: lambda arg1, arg2 : Expresion

#funcion con nombre
#def saludar():
#    print("hola")


# Apartado 1 : Definir una funcion lambda

suma = lambda a, b : a + b

print(suma(5,5))
print(suma(5,15))

saludar = lambda nombre: print(f"hola {nombre}")

saludar("Juan")
saludar("Ana")

# Apartado 2 : Llamar funciones dentro de una lambda
#              dentro de la expresion de una funcion 
#              lambda podemos llamar a otras funciones

maximo = lambda a, b, c: f"El maximo entre {a}, {b} y {c} es {max(a,b,c)}"

print(maximo(3,4,5))
print(maximo(10,99,-25))

# Apartado 3 : Funciones lambda dentro de funciones. 
# Podemos definir funciones lambda dentro de funciones convensionales.

# Esto nos permite generar funciones lambda con distintos parametros.

def ponerPrefijo(prefijo):
    return lambda nombre : f"{prefijo} {nombre}"

addMr = ponerPrefijo("Mr")
addSr = ponerPrefijo("Sr")
addMis = ponerPrefijo("Miss")

print(addMr("Juan"))
print(addSr("Julian"))
print(addMis("Nerea"))

def elevarA(exponente):
    return lambda base: base ** exponente

elevarAlCuadrado = elevarA(2)
elevarAlCubo = elevarA(3)

print(elevarAlCuadrado(3))
print(elevarAlCubo(2))
