# Programacion Orientada a Objetos 
# Herencia

# La herencia es uno de los pilares de la POO.

# Es un mecanismo o funcionalidad que permite que una clase
# reciba todas las caracteristicas, metodos y atributos, de 
# otra clase.

# La clase que hereda, tendra todos los metodos y atributos de
# la clase de la cual esta heredando. ademas tendra tambien los 
# suyos propios.

# Nomenclatura de la herencia

# Superclase : tambien conocida como clase padre. Es la clase de 
#              la cual se heredan las caracteristicas. Suele ser
#              mas general y sirve de base para otras clases.

# Subclase : Tambien conocida como clase hijo. Es la clase que recibe
#            la herencia y amplia los metodos y atributos de la superclase
#            con los suyos propios. Suele ser una clase mas concreta o especifica

# Ejemplo

#    Clase mama 
#    atributos:
#    nombre
#    edad 
#    trabaja
#    jubilado

#    clase hijo
#    atributos: 
#    nombre 
#    edad 
#    trabaja 
#    jubilado
#    estudia

# Tipos de herencia

# 1. La herencia simple es la forma mas basica de herencia que existe, como su nombre
# bien indica

# OJO una subclase hereda de una superclase

# 2. La herencia Jerarquica : se produce cuando multiples subclases heredan de una superclase

# 3. La herencia Multiple : se genera cuando una subclase hereda de dos superclases al mismo tiempo

# 4. La herencia multinivel : esta se genera cuando una subclase hereda de una superclase, a su vez
# esta superclase hereda de otra superclase.

# Ejemplo caso 1

class Persona():
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def presentarse(self):
        print(f"Hola me llamo {self.nombre} y tengo {self.edad} años")

class Trabajador(Persona):
    def __init__(self, nombre, edad, dni, sueldo, cargo, empresa):
        super().__init__(nombre, edad, dni)
        self.sueldo = sueldo
        self.cargo = cargo
        self.empresa = empresa
    
    def calcularSueldoAnual(self):
        return 12 * self.sueldo + 2000

# Caso 2

class Estudiante(Persona):
    def __init__(self, nombre, edad, dni, universidad, curso, asignatura):
        super().__init__(nombre, edad, dni)
        self.universidad = universidad
        self.curso = curso
        self.asignatura = asignatura

    def describirse(self):
        print(f"Hola soy {self.nombre}. Tengo {self.edad} años y estudio en la universidad {self.universidad}\nEstoy en el curso {self.curso}")

# Caso 3

class Telefono:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def llamada(self):
        print("LLamando al *5 numero de ayuda al cliente")
    
class Smartphone:
    def __init__(self, versionAndroid, almacenamiento, memoria):
        self.versionAndroid = versionAndroid
        self.almacenamiento = almacenamiento
        self.memoria = memoria

    def sistemaOperativo(self):
        print(f"Tu version de telefono es {self.versionAndroid}")

class Tablet(Smartphone, Telefono):
    def __init__(self, versionAndroid, almacenamiento, memoria, marca, modelo, pantalla, camara):
        Smartphone.__init__(self, versionAndroid, almacenamiento, memoria)
        Telefono.__init__(self, marca, modelo)
        self.pantalla = pantalla
        self.camara = camara
    
    def tipoDePantalla(self):
        print(f"La pantalla de la tablet es de {self.pantalla} px")

# Caso 4 

class coche:
    def __init__(self, ruedas, marca, tipo):
        self.ruedas = ruedas
        self.marca = marca
        self.tipo = tipo
        self.consume = None        

    def cuentaRuedas(self):
        print(f"El coche tiene {self.ruedas} rueda(s)")

    def tipoCoche(self):
        if(self.tipo == "hibrido"):
            self.consume = "gas"
        else:
            self.consume = "gasolina"
        print(f"Tu coche es {self.tipo} y consume {self.consume}")

class moto(coche):
    def __init__(self, ruedas, marca, tipo, cilindros, transmision):
        super().__init__(ruedas, marca, tipo)
        self.cilindros = cilindros
        self.transmision = transmision
    
    def descripcion(self):
        print(f"La marca de la moto es {self.marca}")

    def numeroDeCilindros(self):
        print(f"La moto tiene {self.cilindros} cilindros")

class lancha(moto):
    def __init__(self, ruedas, marca, tipo, cilindros, transmision, tipoDeMotor):
        super().__init__(ruedas, marca, tipo, cilindros, transmision)
        self.tipoDeMotor = tipoDeMotor
    
    def preparaLancha(self):
        print(f"preparando motor de {self.tipoDeMotor}")

# Bloque de entrada 3
"""
bmw = coche(4,"bmw","normal")
bmw.cuentaRuedas()
bmw.tipoCoche()

kawasaki = moto(2,"kawasaki","hibrida","125cc","sincronica")
kawasaki.numeroDeCilindros()
kawasaki.descripcion()

garin = lancha(0, "garin", "mar", 200, "automatica", "fuera de borda")
garin.preparaLancha()
"""

# Bloque de entrada 2
"""
xiaomi = Tablet(10, 122, 8, "Xiaomi", "M42K", "1080", 24)
xiaomi.llamada()
xiaomi.sistemaOperativo()
xiaomi.tipoDePantalla()
"""
#Bloque de entrada 1
"""
oscar = Persona("Oscar", 23, "72312525G")
oscar.presentarse()
print(oscar.dni)
"""
"""
trabajador = Trabajador("Jose", 29, "92345612H", 1080, "Programador", "Gugle")
trabajador.presentarse()
print(trabajador.dni)
print(trabajador.cargo)
print(trabajador.sueldo)
print(trabajador.calcularSueldoAnual())
"""

"""
estudiante = Estudiante("Maria", 20, "123473523V", "Universidad de Madrid", 3, ["Programacion", "calculo", "algebra"])

estudiante.describirse()
"""