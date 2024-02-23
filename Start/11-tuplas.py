# Capitulo 11 : Las tuplas

# Apartado 1 : Tuplas - Concepto basico
# Son conjundo ordenados de datos que no se pueden modificar
"""
mitupla = ("audifonos", "raton", "boligrafo", "cuaderno", "telefono","cargador")

print(mitupla)
print(f"Longitud de la tupla: {len(mitupla)}")

for objetos in mitupla:
    print(f"Cantante numero: {mitupla.index(objetos)} es {objetos}")
"""
# Apartado 2 : Indexado
# Podemos indexar los elementos de una tupla de la misma forma que las listas
"""
mitupla = ("audifonos", "raton", "boligrafo", "cuaderno", "telefono","cargador")

primero = mitupla[0]
ultimo = mitupla[-1]
subtupla = mitupla[1:3]

print(f"Este es mi primer elemento de la tupla: {primero}")
print(f"Este es mi ultimo elemento de la tupla: {ultimo}")
print(f"Este es mi subtupla de la tupla: {subtupla}")
"""
# Apartado 3 : Modificacion de tuplas

# No podemos modificar directamente una tupla. Veremos que errores ocurren
# y como transforma una tupla en una lista y viceversa.
"""
mitupla = ("audifonos", "raton", "boligrafo", "cuaderno", "telefono","cargador")

lista = list(mitupla)
print(lista)
print(type(lista))

lista.insert(1, "pendrive")

tupla = tuple(lista)
print(tupla)
print(type(tupla))
"""
# Apartado 4 : Empaquetar y desempaquetar tuplas

# De la misma forma que podemos agrupar multiples variables en una tupla (empaquetar).
# Tambien podemos asignar cada elemento de una tupla a una variable distinta.
"""
mitupla = ("audifonos", "raton", "boligrafo", "cuaderno", "telefono","cargador")

material = "Papel"
material2 = "Carton"

tupla2 = (material, material2)
print(tupla2)

tupla3 = ("audifonos", "raton", "boligrafo")

(obj1, obj2, obj3) = tupla3
print(f"Objetos fuera de la mesa: {obj1}, {obj2} y {obj3}")

(obj1, obj2, obj3, *varios) = mitupla
print(f"En la mesa tienes : {obj1} , {obj2} y {obj3}")

(obj1, *varios, objFinal) = mitupla
print(f"Mi primer objeto es {obj1} y el ultimo objeto es {objFinal}")
print(f"Objetos en el baul : {varios}" )
"""
# Apartado 5 : "Extra" lista de tupla

# Podemos crear listas cuyos elementos sean tuplas. De esta forma, podemos iterar sobre
# las diversas tuplas y ademas desempaquetar sus elementos.

comidas = [(1, "Sopa de pollo"), (2, "Arroz a la putanesca"), (3, "Arroz con leche")]
print("El menu de hoy es ")

for plato, comida in comidas:
    print(f"Plato nº: {plato} - {comida}")

diccionario = {1 : "Blanco", 2 : "Azul", 3: "Rojo", 4: "Verde"}
elementos = diccionario.items()
print(elementos)

for clave, valor in elementos:
    print(f"Clave: {clave} ------> {valor}")