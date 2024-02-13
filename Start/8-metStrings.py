# Capitulo 8 - Metodos de String
# Apartado 1 - find, index y count
# Los metodos find e index siven para encontrar conjuntos 
# de caracteres dentro de un string (por ejemplo una palabra dentro de una frase)
"""
texto = "correo@gmail.com"
posicion = texto.index("@")
print(posicion)

posicion = texto.find("@")
print(posicion)

#posicion = texto.find("*")
#print(posicion)

#posicion = texto.index("*")

posicion = texto.index("@")

repeticiones = texto.count("r")
print(f"la letra r se repite {repeticiones} veces")
"""
# Apartado 2 - split, replace y join
# El metodo split sirve para dividir un string mediante un delimitador
# y convertir cada division en un elemento de una lista

# El metodo replace sirve para reemplazar un substring por otro

# El metodo join sirve para unir una lista de strings en unico string 
# mediante un caracter determinado
"""
compra = "Chocolate, pan, agua, platanos, pipas, verduras"
compra2 = "Chocolate pan agua platanos pipas verduras"

listaCompra = compra.split(', ')
listaCompra2 = compra.split()

print(listaCompra)
print(listaCompra2)
print(f"En la lista de la compra tenemos {len(listaCompra)} productos")

compraGuiones = compra.replace(', ', ' - ')
print(compraGuiones)

lista = " / ".join(listaCompra)
print(lista)
"""
# Ejercicio - Tenemos unas descripciones de algunos productos.
# en ella se incluye el precio de cada producto. Debemos encontrar el precio en €
# y mostrarlo por pantalla. el precio puede tener:
# 0.1 y 2 decimales y siempre seguido del simbolo '€' por ejemplo:
# 
# 9.99 €
# 10 €
# 10.5 €
#
# Bonus: Debemos modificar las descripciones para que el precio se muestre en dolares.
#        La conversion es de 1 € ---> 1.21 $ no hace falta modificar la variable
#        original de la descripcion, podemos retomar una copia con el precio convertido
"""
def findValueWithCasting(txt):
    txtLista = txt.split()
    posicion = -1
    indx = -1
    conversion = 1.21
    for palabra in txtLista:
        posicion = palabra.find("€")
        if(posicion != -1):
            indx = txtLista.index(palabra)
            break    
    
    precio = txtLista[indx]
    precio = precio.split("€")[0]
    txtLista[indx] = str(round(float(precio)*conversion, 2)) + '$'
    nuevaDescripcion = " ".join(txtLista)

    return precio, nuevaDescripcion
    
des1 = "Este bolso de cuero de la marca: Miguel Cors tiene un precio de 199.99€. Es una oferta especial."
des2 = "Las botas de la marca: Nike valen 89€. Nunca han estado tan rebajadas"
des3 = "! Tenemos el banbu en oferta ! Compralo por 1.89€ el kg no dejes pasar esta oportunidad"

precio, descripcion = findValueWithCasting(des1)
print(precio)
print(descripcion)

precio, descripcion = findValueWithCasting(des2)
print(precio)
print(descripcion)

precio, descripcion = findValueWithCasting(des3)
print(precio)
print(descripcion)
"""
# Apartado 3 - Otros metodos utiles
# En este apartado veremos algunos metodos que pueden ser de utilidad
# para manipular strings.
"""
texto = "este es un texto de prueba"
print("Metodo starwith: ")
print(texto.startswith("esto"))
print("Metodo upper: ")
print(texto.upper())
print("Metodo title: ")
print(texto.title())
print("Metodo capitalize")
print(texto.capitalize())
print("Metodo rjust: ")
print(texto.rjust(len(texto) + 8))
"""
# Ejercicio: Formatear texto. Debemos formatear el siguiente texto siguiendo una serie de normas
#  ------ Si tiene # :  a principio de linea significa que es un titulo y deberemos convertirlo
#                       todo a mayusculas.
#  ------ Si tiene ## : a principio de linea significa que es un sutitulo y deberemos poner la
#                       primera letra de cada palabra en mayuscula
#  ------ Si tiene ###: deberemos poner unicamente la primera letra en mayuscula
#  ------ Si tiene -  : Deberemos poner una sangria

# Nota: el metodo splitlines() retorna una lista de strings. Separa mediante saltos de linea

texto = """
# este es el titulo principal

- Esto es una lista
- De cosas que podemos hacer.

##  este es un subtitulo

Esto es una pequeña introduccion.
- esto es otra lista
- de mas cosas que podemos hacer.

### Este es un subtitulo
- Continuacion
"""

def formatText(texto):
    listaTexto = texto.splitlines()
    for idx in range(len(listaTexto)):
        if(listaTexto[idx].startswith("###")):
            listaTexto[idx] = listaTexto[idx].replace("###", "")
            listaTexto[idx] = listaTexto[idx].capitalize()
        if(listaTexto[idx].startswith("##")):
            listaTexto[idx] = listaTexto[idx].replace("##", "")
            listaTexto[idx] = listaTexto[idx].title()
        if(listaTexto[idx].startswith("#")):
            listaTexto[idx] = listaTexto[idx].replace("#", "")
            listaTexto[idx] = listaTexto[idx].upper()
        if(listaTexto[idx].startswith("-")):
            listaTexto[idx] = listaTexto[idx].rjust(len(listaTexto[idx]) + 8)
    return "\n".join(listaTexto)
    
print(formatText(texto))