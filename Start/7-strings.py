# Capitulo 7 - Cadena de caracteres o Strings
# Apartado 1 : Repaso de conceptos basicos
"""
texto = "Hola Que Tal"
print(texto)

textoConComillas = 'Has escrito con las comillas'
print(textoConComillas)

stringConFormato = ' triple comillas aqui '
*************************************
*****   Este es un formato   ********
    1. Enumeracion de contenido
    2. Enumeracion de contenido
    3. Enumeracion de contenido

print(stringConFormato)

cadena = 0123456789
print("El string tiene una logitud de: ")
print(len(cadena))

"""
# Apartado 2 : ¿ Los strings son listas ?
# En este apartado descubriremos que los strings son realmente arrays
# o vectores (similares a una lista)
"""
texto = '0123456789'
primerCaracter = texto[0]
subString = texto[1:5]

print("El texto original es : " + texto)
print("El primer caracter es: " + primerCaracter )
print("El substring es :" + subString)
"""
# Ejercicio : Tenemos un string unicamente compuesto por numeros enteros
#             debemos sumar su valor uno a uno y mostrar por pantalla
#             la suma total de todos los numeros
"""
texto = "124612623"
sumaTotal = 0
for numero in texto:
    castingNumero = int(numero)
    sumaTotal += castingNumero
print(sumaTotal)
"""
# Apartado 3 : Format Strings
#              Nos permite generar strings combinado texto
#              con otras variables de forma legible y sencilla

cantidad = 7
precio = 1.80

print("Forma Cutre")
print("Has comprado "+ str(cantidad) + " botellas. Cada botella cuesta " + str(precio) + "$ y el total es "+ str(cantidad * precio)+ "$")

print("Forma Avanzada")
print("Has comprado {} botellas. Cada botella cuesta {} $ y el total es {} $".format(cantidad, precio, cantidad*precio))

print(f"Has comprado {cantidad} botellas. Cada botella cuesta {precio} $ y el total es {cantidad*precio} $")