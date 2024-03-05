# Capitulo 20 : Funcion Map y Filter
# Son funciones que sirven para trabajar con objetos iterables.
# Vienen incorporadas por defecto con python.

# Apartado 1: Funcion Filter
# filter(function, iterable). Devuelve un iterador
# con los valores del iterable que cumple la funcion

import math

# Metodo adecuado
def evaluarEmail(email):
    # Metodo 2:
    return '@' in email
    # Metodo 1:
    #if '@' in email:
    #    return True
    #else:
    #    return False

emails = [
    'juan@hotmail.com',
    'javier@gmail.com',
    'mandarinas',
    'wikipedia.com'
]

"""
# Metodo inicial
emailsValidos = []
for email in emails:
    if '@' in email:
        print(f"el email {email} es valido")
        emailsValidos.append(email)
    else:
        print(f"El email {email} es invalido")

print(emailsValidos)
"""

# Uso de la funcion filter para comprobar emails validos de una lista

"""
emailsValido = list(filter(evaluarEmail, emails))
print(emailsValido)

#print(next(emailsValido))
#print(next(emailsValido))

"""

# Uso de la funcion filter con una funcion lambda
"""
emailsValido = list(filter(lambda email: '@' in email, emails))
print(emailsValido)
"""
# Apartado 2 : Funcion map
# map(function, iterable),
# Ejecuta la funcion usando como parametro cada elemento
# Va pasando por posicion cada cadena de caracteres y saca la longitud de la palabra

palabras = ['dale', 'un', 'buen', 'like', 'y', 'suscribete']

longitudes = list(map(lambda palabra: len(palabra), palabras))
print(longitudes)

eje_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
eje_xx = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
eje_y = list(map(lambda x,y: round(math.cos(x) + math.exp(y), 2), eje_x, eje_xx))

print(eje_y)