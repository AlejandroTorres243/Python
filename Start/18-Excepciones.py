# Capitulo 19 : Excepciones

# Las excepciones son errores que ocurren durante la ejecucion del programa.
# Estos errores surgen a pesar de que la sintaxis sea correcta.

# Ejemplos

#  - Acceder a una posicion de una lista superior a la longitud de esta.
#    ERROR  DE LONGITUD
#  - Intentar abrir un fichero que no existe
#  - Convertir una cadena de texto a int

# IMPORTANTE: Gestionar las excepciones nos permite que el codigo se siga
#             ejecutando a pesar de que ocurran errores.

import logging

"""
def division(a, b):
    try:
        resultado = a / b
        print(resultado)

    except ZeroDivisionError:
        print("No se puede dividir por cero")

division(5, 5)
division(10, 0)
"""
# Apartado 2 : Gestion de distintos tipos de excepciones
"""
def elegirFruta(listaFrutas):
    try:
        print(listaFrutas)
        index = int(input("Elige tu fruta (pon el numero): "))
        print(f"Tu fruta favorita es {listaFrutas[index]}")
    except IndexError:
        print(f"Indice incorrecto debe esta estar entre cero y {len(listaFrutas)-1}")
    except ValueError:
        print("Tienes que poner un numero entero")

frutas = ["0-Platano", "1-Manzana", "2-Pomelo", "3-Melocoton"]
elegirFruta(frutas)
"""
# Apartado 3 : Excepcion exception
# Las excepciones son objetos que heredan de la clase exception
"""
def elegirFruta(listaFrutas):
    try:
        print(listaFrutas)
        index = int(input("Elige tu fruta (pon el numero): "))
        print(f"Tu fruta favorita es {listaFrutas[index]}")
    except Exception as errorRandom:
        #print("Ha ocurrido un error, algo ha salido mal")
        logging.exception("El error es el siguiente: ")

frutas = ["0-Platano", "1-Manzana", "2-Pomelo", "3-Melocoton"]
elegirFruta(frutas)
"""
# Apartado 4: Else, Finally, Raise
# Vamos a sumar los numeros que nos pase el usuario separados por espacios

while True:
    try:
        total = 0
        sumandos = input("Ponme numeros separados por espacios: ")
        sumandos = sumandos.split()
        for num in sumandos:
            if num.isnumeric():
                total += float(num)
            else:
                raise ValueError("El valor no es un numero")
    except ValueError:
        print("Los datos son incorrectos")
        print("Vuelve a introducir los numeros")
    else: 
        print(f"El valor de la suma es {total}")
        break
    finally:
        print("Ha terminado la iteracion")