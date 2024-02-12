# Capitulo 6 - Listas
# Apartado 1 : Repaso de conceptos generales
"""
cadena = [1, 2, 3, 4, 5]
primeraPosicion = cadena[0]
longitudCadena = len(cadena)

print("Primer elemento de la cadena: "+ str(primeraPosicion) + "\nLongitud de la cadena: " + str(longitudCadena))

for numero in cadena:
    print(numero)
"""
# Apartado 2 : Indexado y sublistas

"""
lista = ["Dale", "un", "buen", "like", "para", "mas", "contenido", "como", "este"]
print(lista)
ultimaPosicion = lista[-1]
print(ultimaPosicion)
penultimo = lista[-2]
print(penultimo)

# Sublistas

# sublista = lista[limite-inferior:limite-superior]
# Los limites son posiciones de la lista

sublista = lista[1:4]
print(sublista)
sublista = lista[:4]
print(sublista)
sublista = lista[2:]
print(sublista)

# Indexado

sublista = lista[-4:-1]
print(sublista)
"""

# Apartado 3 : Comprobar si una lista tiene contiene un elemento o no
"""
lista = ["Dale", "un", "buen", "like", "para", "mas", "contenido", "como", "este"]
primeraPalabra = "Dale"
segundaPalabra = "Mas"

if primeraPalabra in lista:
    print("La palabra pertenece a la lista")

if segundaPalabra not in lista:
    print("La palabra no se encuentra en la lista")
"""
# Apartado 4 : Modificar elementos en una lista
"""
lenguajes = ["C", "Java", "Python", "JavaScript", "Kotlin", "Ruby", "Scala"]
print(lenguajes)
lenguajes[1] = "Angular"
print(lenguajes)
lenguajes[0] = lenguajes[0] + "++"
print(lenguajes)
lenguajes[2:4] = ["Anaconda", "Typescript"]
print(lenguajes)
lenguajes[4:5] = ["AWS", "Snowflake"]
print(lenguajes)
"""
# Apartado 5 : Metodos de las listas: añadir elementos;
# en Python podemos utilzar metodos con las listas;
# Para ejecutar estos metodos "variableDeTipoLista.metodo()"
"""
lenguajes = ["C", "Java", "Python", "JavaScript", "Kotlin", "Ruby", "Scala"]
print(lenguajes)

lenguajes.insert(1, "C++")
print(lenguajes)

lenguajes.append("R")
print(lenguajes)

frameworks = ["Angular", "React", "VueJS"]
lenguajes.extend(frameworks)
print("Lista 1 : "+ str(lenguajes))

frameworks.extend(lenguajes)
print("Lista 2 :" + str(frameworks))
"""
# Apartado 6 : Metodo de las listas - Eliminar elementos 
"""
frutas = ["Platano", "Kiwi", "Papaya", "Melocoton", "Cereza"]
print(frutas)

frutas.pop()
print(frutas)

elementoEliminado = frutas.pop(0)
print(frutas)
print(elementoEliminado)

frutas.remove("Kiwi")
print(frutas)


del frutas[0]
print(frutas)
"""
# Apartado 7 : Ejercicios

# Enunciado : Tenemos un texto donde queremos encontrar palabras clave
#             La palabra clave puede ser hasta 5 y deberemos pedirselo al usuario
#             y guardarla en una lista.
# 
# Si el usuario quiere poner menos de 5 palabras clave, debera escribir "fin"
# para terminar de introducir datos. Si el usuario introduce numeros o nada,
# se debera eliminar de la lista antes de la busqueda.
# 
# En otra lista, debemos guardar el numero de veces que aparece cada palabra
# clave en el texto. Por ejemplo, si las palabras clave son ordenador y portatil
# y aparece 5 y 7 veces respectivamente nuestras lista deberan de quedar de la
# siguiente manera:
# 
# keyword : ["Ordenador", "Portatil"]  
# ocurrencia : [5, 7]
# 
#  Pista : Podemos pasar de una cadena de texto a una lista de palabras mediante 
#          el metodo texto.split(). Por ejemplo:
#       
# texto = "hola que tal"
# print(texto.split())
# texto = ["hola", "que", "tal"] 

texto = """ Seguramente hayas notado que tu productividad ha bajado desde que trabajas en desde casa
Es muy importante que logremos teletrabajar efectivamente y de manera autoregulada.
Esto se traduce en finalizar antes nuestras tareas y evitar jornadas laborales interminables.
El primer consejo y uno de los mas importantes ya te lo he dado en el apartado anterior.
Tenemos que construir un espacio de trabajo en el que nos sintamos comodos y dispongamos 
de todas las herramientas necesarias para el teletrabajo.
De esta forma, nuestro cerebro asocia el sitio con la accion de trabajar y nos hara estar
mas focalizado en nuestras tareas.
"""

keywords = []
ocurrencias = []

for x in range(5):
    keyword = input("Introduce una palabra o fin para terminar: ")
    if keyword == "fin":
        break
    else:
        keywords.append(keyword) 

print("Lista sin tratamiento")
print(keywords)

posicion = 0
while(True):
    if posicion >= len(keywords):
        break
    if keywords[posicion] == '':
        keywords.pop(posicion)
    elif keywords[posicion].isnumeric():
        keywords.pop(posicion)
    else:
        posicion += 1

print("Lista con tratamiento")
print(keywords)        

texto = texto.split()

for x in range(len(keywords)):
    ocurrencias.append(0)

for palabra in texto:
    for keyword in keywords:
        if keyword == palabra:
            pos = keywords.index(keyword)
            ocurrencias[pos] += 1
            break

print("Lista de ocurrencias")
print(ocurrencias)
