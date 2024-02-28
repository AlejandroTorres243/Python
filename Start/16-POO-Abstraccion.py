# CLASES ABSTRACTAS:
# - NO LAS VAMOS A INSTANCIAR NUNCA DIRECTAMENTE.
# - CONTIENEN POR LO MENOS UN METODO ABSTRACTO
# - LAS VAMOS A USAR DE BASE PARA SUBCLASES MAS ESPECIFICAS.

# METODOS ABSTRACTOS:
# - DEBEMOS SOBREESCIBIRLOS EN CADA UNA DE LAS CLASES

from abc import ABC, abstractmethod

class Personaje(ABC):
    # Decoradores
    # LO QUE HACE ES ENVOLVER Y MODIFICAR EL COMPORTAMIENTO
    # DE LA FUNCION QUE ESTE DECORANDO
    
    @abstractmethod
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 0
        self.inventario = []
        self.vida = 100

    @abstractmethod
    def atacar(self, objetivo):
        pass

    @abstractmethod
    def getStatus(self):
        print(f"Nombre: {self.nombre} Nivel: {self.nivel}")

    def subirDeNivel(self):
        self.nivel += 1
    
    def verInventario(self):
        print(f"Inventario de {self.nombre}")
        for objeto in self.inventario:
            print(objeto)

class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 120
        self.inteligencia = 95
        self.inventario = ["Pocion de Mana", "Grimorio"]

    def getStatus(self):
        print("Clase Mago")
        super().getStatus()
    
    def atacar(self, objetivo):
        objetivo.vida -= self.inteligencia * 0.6
        print(f"La vida actual del objetivo es {objetivo.vida}")
        
    def saludar(self):
        print("Hola que tal soy un mago")

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 200
        self.fuerza = 75
        self.inventario = ["Pocion de vida", "Escudo", "Espada"]

    def getStatus(self):
        print(f"Clase Guerrero")
        super().getStatus()

    def atacar(self, objetivo):
        objetivo.vida -= self.fuerza * 0.8
        print(f"El objetivo se ha quedado con {objetivo.vida} puntos de vida")

guerrero = Guerrero("Kaladin")
mago = Mago("Yuno")

guerrero.getStatus()
mago.getStatus()

mago.verInventario()
guerrero.verInventario()

mago.atacar(guerrero)
guerrero.atacar(mago)

