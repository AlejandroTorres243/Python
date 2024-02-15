# Capitulo 9 - Diccionarios
# Apartado 1 - Conceptos basicos
# 
# Declaracion de diccionarios:
# Los diccionarios son conjuntos de elementos con la estructura clave : valor.
# Cada elemento de un diccionario contiene una clave y un valor asociado a este.
# Las claves pueden ser de tipo string o int. Los valores pueden ser cualquier tipo de dato.
"""
alejandro = {"Nombre": "Alejandro", "Edad": 32, "Ciudad":"Barcelona", "Aficiones":["Lectura", "Cine", "Videojuegos"]}
print(alejandro)
ana = {"Nombre": "Ana", "edad": 42, "Ciudad": "Madrid", "Aficiones":["Pesca", "Natacion", "Escritora", "Cantar"]}
print(ana)

trabajadores = {0: alejandro, 1: ana}

print(f"La longitud del diccionario de alejandro es {len(alejandro)}")
print(f"La longitud del diccionario de trabajadores es {len(trabajadores)}")

print("Claves duplicadas")
dic = {"año": 1990, "año": 2003, "otra clave": "clave", "año":2005}
print(dic)
"""
# Apartado 2 - Añadir, eliminar y modificar elementos de un diccionario
"""
alejandro = {"Nombre": "Alejandro", "Edad": 32, "Ciudad":"Barcelona", "Aficiones":["Lectura", "Cine", "Videojuegos"]}
print(alejandro)

print("Como agregar en un diccionario")

alejandro["cargo"] = "CEO"
print(alejandro)

alejandro.update({"sueldo": 9000, "vacaciones": "si"})
print(alejandro)

print("Como eliminar en un diccionario")
del alejandro["vacaciones"]
print(alejandro)

valor = alejandro.pop("cargo")
print(f"El cargo de {valor} se a eliminado")
print(alejandro)

print("Como acceder a un elemento de un diccionario")
edad = alejandro["Edad"]
print(f"la edad de alejandro es {edad}")
alejandro["Edad"] = 34
alejandro.update({"Ciudad": "Zaragoza"})
alejandro["Aficiones"].insert(1,"Cocina")
alejandro["Aficiones"].append("Carpinteria")

print(alejandro)
"""
# Apartado 3 - Lista de claves y valores
# Podemos obtener una lista tanto de las claves como de lo valores que conforman un diccionario
"""
alejandro = {"Nombre": "Alejandro", "Edad": 32, "Ciudad":"Barcelona", "Aficiones":["Lectura", "Cine", "Videojuegos"]}

for clave, valor in zip(alejandro.keys(), alejandro.values()):
    print(f"{clave} -> {valor}")

for clave, valor in alejandro.items():
    print(f"{clave} ===> {valor}")
"""
# Ejercicio: Buscador de productos. Tenemos varios productos, el usuario
# mediante el nombre de un producto puede consultar su precio y sus unidades en stock.

pantalones = {
    "nombre": "Pantalones",
    "precio": 39.99,
    "cantidad": 5
}

chaquetas = {
    "nombre": "chaquetas",
    "precio": 49.99,
    "cantidad": 15
}

bufandas = {
    "nombre": "bufandas",
    "precio": 5.45,
    "cantidad": 3
}

zapatos = {
    "nombre": "zapatos",
    "precio": 24.99,
    "cantidad": 9    
}

productos = [pantalones, chaquetas, bufandas, zapatos]

def askForInfo(nombreProducto):
    print(productos)
    for producto in productos:
        print(producto)
        if(producto["nombre"]== nombreProducto):
            return producto["precio"], producto["cantidad"]
        #else:
        #    return 0, 0
    return 0, 0


nombre = input("¿ Que producto estas buscando ? -> ")
precio, cantidad = askForInfo(nombre)
if(precio == 0 and cantidad == 0):
    print("Lo sentimos, no existe dicho producto")
else: 
    print(f"el producto {nombre} vale {precio} euros y tenemos {cantidad} unidad(es)")
