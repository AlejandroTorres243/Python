# Capitulo 20: Modulos y Paquetes
# Apartado 1: Modulos y paquetes
# Los modulos son archivos de Python.
# Estos archivos pueden contener funciones, clases y variables.
# Podemos importarlas a nuestros archivos para hacer uso de estas
# sin tener que volver a escribir su codigo.

"""
import Modulo_21
from Modulo_21 import areaCuadrado, areaTriangulo
from Modulo_21 import *
"""

"""
print(Modulo.PI)
print(Modulo.areaCirculo(5))
print(Modulo.areaCuadrado(3))
print(Modulo.areaTriangulo(2,3))
"""

# Los paquetes son conjuntos de modulos, relacionados entre si,
# en un mismo directorio

from Paquete_21.Modulo2 import calculaPerimetro as clase
from Paquete_21.Modulo import areaCirculo as cp

funcion = cp(2)
classe = clase.perimetroCirculo(2,4)

print(funcion)
print(classe)