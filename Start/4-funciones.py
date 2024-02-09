# Capitulo 4 : Funciones   
#   Definicion de funciones
def saludar():
    print("Hola que tal")

# saludar()
# saludar()

# Funciones con argumentos 
def saludarDos(nombre):
    print("Hola " + nombre + " como estas")

#saludarDos("Marta")
#saludarDos("Dima")

# Funciones con retorno
def suma(a, b):
    resultado = a + b
    return resultado
 
valor = suma(10, 15)
print(valor)

def sonIguales(num1, num2):
    return num1 == num2

verdad = sonIguales(3, 3)
if(verdad):
    print("Es igual - " + str(verdad))
else:
    print("Es falso - " + str(verdad))

# Funciones con argunmentos con valor por defecto
def saludoPorDefecto(nombre="Jose"):
    print("hola "+ nombre+ " como estas")

#saludoPorDefecto()
#saludoPorDefecto("Andrea")
 
# Funciones que retornan varios valores
def sumaYresta(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    return suma, resta

resultado1, resultado2 = sumaYresta(15, 5)
print("Los resultados son \nSuma: "+str(resultado1) + "\nResta: " + str(resultado2))
 
# Ejercicio 1 : Funcion maximo -> Dado dos numeros, la funcion debe encontrar cual
#  de los dos es el mas grande y retornarlo. Extra: se deben comprobar los argumentos
#  de la funcion, sean del tipo int o float. Si alguno de los dos no lo es, mostrar
#  un mensaje de error y retornarlo false.

def maximo(a, b):
    if(type(a) == int or type(a) == float and type(b) == int or type(b) == float):
        if(a > b):
            print(a)
            return a 
        elif(b > a):
            print(b)
            return b 
        else:
            print("Ambos numeros son iguales, no hay maximo")

maximo(5, 15)
maximo(12, 7)
maximo(12, 12)

# Ejercicio 2: Mini calculadora. Pedirle al usuario una operacion y dos numeros.
# las operaciones pueden ser suma, resta, potencia. Si introduce una operacion 
# diferente a estas. Mostrar un mensaje de error. Y si la operacion es correcta
# mostrar el resultado.

def calculadora():
    a = int(input("Numero 1: "))
    b = int(input("Numero 2: "))
    op = input("Seleccione un numero: 1.Suma / 2. Resta / 3. Potencia: ")    
    if(int(op) == 1):
        print(a + b)
        #return a + b
    elif(int(op) == 2):
        print(a - b)
        #return a - b
    else:
        print(a**b)
        #return a**b

calculadora()