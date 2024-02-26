# Capitulo 14 - Encapsulamiento

# Es uno de lo pilares de la programacion orientada a objetos POO
# Permite regular el acceso a los metodos y atributos de una clase
# En cierta manera, enmascara la complejidad de una clase

# Modificadores de acceso

# Publicos 
#  Son accesibles por :
#  - Cualquier punto de codigo 
#  - Dentro / Fuera de la clase subclases

# Protegidos 
#  Son accesibles por :
#  - La misma clase 
#  - Las subclases
#  - Clases dentro del mismo paquete

# Privados
#  Son accecibles por :
#  - Unicamente dentro de la misma clase

# Utilidades del encapsulamiento
# Nos permite ocultar metodos y atributos afuera de la propia clase.
# Podemos regular la modificacion de los atributos (privados) evitando
# que se accedan a ellos directamente. Crea metodos (publicos) para modificar
# los atributos de un objeto.
# Enmascara la complejidad de algunos metodos, haciendolos privados y utilizandolos
# desde metodos publicos.

# Existe una convencion, pero es solo sintaxis, no es funcional:

# _atributo = "atributoProtegido". Un guion bajo al principio del nombre de un atributo
# Indica que es protegido

# __atributo = "atributoPrivado". Un doble guion bajo al principio del nombre de un
# atributo indica que es privado

# La misma sintaxis para los metodos.

# Para Python todos los atributos y metodos son PUBLICOS. La convencion simplemente
# se usa entre programadores para indicar como se debe usar los metodos y atributos
# de una clase.

# Ejemplo:

class Circulo:
    def __init__(self, radio):
        self.__radio = radio
        self.__pi = 3.1415

    def calcularPerimetro(self):
        return 2*self.__pi*self.__radio

    def calcularArea(self):
        return self.__pi*self.__radio**2

    def getPi(self):
        return self.__pi

    def setRadio(self, nuevoValor):
        if(type(nuevoValor) == int or type(nuevoValor) == float):
            if(nuevoValor > 0):
                self.__radio = nuevoValor
                print("Modificacion exitosa")
            else:
                print("El radio no puede ser negativo")
        else:
            print("El radio tiene que ser un numero positivo")

c2 = Circulo(2.5)
print(c2.calcularArea())
print(c2.calcularPerimetro())
#print(f"El valor de pi es {c2.pi}")
print(f"El valor de pi es {c2._Circulo__pi}")
print(f"El valor de pi es {c2.getPi()}")

# El acceso es __radio -> _Circulo__radio .
# En general _nombreDeLaClase__nombreDelAtributo

c2.setRadio(45)
c2.setRadio(-45)
c2.setRadio("Hola Mundo")
