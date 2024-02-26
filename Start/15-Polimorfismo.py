# El polimorfismo es la accion de redefinir varios metodos de una clase padre en una clase hija de 
# distintas formas

# Polimorfismo es una herramienta que nos va a permitir redefinir metodos que heredemos de una clase padre
#Por ejemplo si se define un metodo en una super clase y luego ese mismo metodo
#heredan 3 subclases el mismo metodo en cada una de estas subclases se podra redefinir el mismo metodo
#de distintas maneras

class Empleado():
    def __init__(self, nombre, sueldoMensual):
        self.nombre = nombre
        self.sueldoMensual = sueldoMensual

    def calcularSueldoAnual(self):
        sueldo = 12*self.sueldoMensual*(1+1/100)
        print(f"El sueldo anual de {self.nombre} , empleado normal, es de {sueldo}")

class Contable(Empleado):
    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual)

    def calcularSueldoAnual(self):
        sueldo = 12*self.sueldoMensual*(1+ 4/100)
        print(f"El sueldo anual de {self.nombre}, contable, es de {sueldo}")

class Publicista(Empleado):
    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual)

    def calcularSueldoAnual(self):
        sueldo = 12 * self.sueldoMensual * (1 + 5/100)
        print(f"El sueldo anual de {self.nombre}, publicista, es de {sueldo}")

class Becario(Empleado):
    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual)

    def calcularSueldoAnual(self):
        sueldo = 12 * self.sueldoMensual
        print(f"El sueldo anual de {self.nombre}, becario, es de {sueldo}")

empleados = [
    Empleado("Juan", 1000),
    Contable("Angela", 1100),
    Publicista("Ryan", 1200),
    Becario("Neil", 750)
]

for empleado in empleados:
    empleado.calcularSueldoAnual()