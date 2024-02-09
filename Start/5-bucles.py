# Capitulo 5 : Bucles
# ------------ Parte I ---------------
# Breve introduccion a las listas
numeros = [1,2,3,4,5]
print(numeros)
print(numeros[0])
print(numeros[2])
print(len(numeros))

texto = ["Juan", "Botella", "Taza", "Macarrones"]
print(texto[1])
print(texto[len(texto)-1])

# Bucle for

for x in range(1, 10):
    print(x)

print("Fin del bucle")

for x in range(5, 26, 5):
    print(x)

print("Fin del bucle")

# Mini ejemplo. Imprimir solo las vocales de una palabra
palabra = "bibliotecario"
for vocal in palabra:
    if (vocal == 'a' or vocal == 'e' or vocal == 'i' or vocal == 'o' or vocal == 'u'):
        print (vocal)


# Mini ejemplo, iterar sobre una lista

"""numeros = [11, 22, 33, 44, 55]

for indice in range(len(numeros)):
    numeros[indice] += 12

print(numeros)"""

# Bucles while
"""contador = 0

while(contador < 10):
    print(contador)
    contador += 1
"""

letraEncontrada = False
letra = "a"
frase = "En este momento estoy buscando la letra a"
indice = 0

while(not(letraEncontrada)):
    if(frase[indice] == "a"):
        letraEncontrada = True
        print(f"Hemos encontrado la letra {letra} en el indice {indice}")
    else:
        indice += 1

# ----------------- Parte 2 -------------------- 
# Break, continue, pass
# 

# break

bandera = False
letra = 'y'
cadena = 'En este momento estoy bucando la letra a'

for caracter in cadena:
    if(caracter == letra):
        print(f"La letra {letra} la hemos encontrado en el indice {frase.index(caracter)}")
        break
    else:
        print("No se ha encontrado la letra")

# Continue

frase = "Hola Ana"
caracter = "a"
count = 0

for cad in frase:
    if(cad == caracter):
        count += 1
        print(f"Letra encontrada {count}")
        continue
    print("No se ha encontrado la letra")

# Pass

cadena1 = [10, 5, 81, 17]

for indice in cadena1:
    if(indice == 81):
        pass
    print(f"El valor de la cadena es {indice}")

# Else

frase1 = "Transferencia linea 1"
count1 = 0
for caracter in frase1:
    count1 += 1
    if(caracter == "l"):
        break
    else:
        print(f"La frase tiene {count1} caracteres")

# Ejercicio 1 : el usuario debe adivinar un numero entre 0 y 10
# el programa debe pedir que el usuario introduzca un numero
# y debe decir si acertado, si el numero a divinar es menor o mayor
# que el introducido

numeroAadivinar = 6
numeroEncontrado = False

while(not(numeroEncontrado)):
    numeroIntro = int(input("Introduzca un numero entre 1 y 10: "))
    if(numeroIntro > numeroAadivinar):
        print("El numero introducido es mayor. Intenta de nuevo")
    elif(numeroIntro < numeroAadivinar):
        print("El numero introducido es menor. Intenta de nuevo")
    else:
        numeroEncontrado = True
        print("El numero se ha encontrado")