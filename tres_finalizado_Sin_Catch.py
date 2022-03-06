# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 17:40:29 2022

@author: Manuel
"""
import random

def display_board(board):
  #function para pintar el tablero
    print(board[0][0],"|",board[0][1],"|",board[0][2])
    print("--*---*--")
    print(board[1][0],"|",board[1][1],"|",board[1][2])
    print("--*---*--")
    print(board[2][0],"|",board[2][1],"|",board[2][2])

# funciones adicionales (a trozos)
##############################################################################

# Funcion que crea la posible lista de posiciones de cada juego
def comienzo_de_turno(indiceboard):
    orden = []
    cont = 0
    while(cont < len(indiceboard)):
        comienza = random.randint(0, 1)
        if(len(orden)==0):
              orden.append(comienza)
        else:
             for x in orden:
                 if((comienza == orden[-1]) and (orden[-1] == 0)):
                     comienza = 1
                 if((comienza == orden[-1]) and (orden[-1] == 1)):
                     comienza = 0
             orden.append(comienza)
        cont+=1     
    return orden    

#Funcion que crea y chequea valores para el ordenador
def chequeo_valor_pc(indice, numMax):
      randpos = random.randint(1,numMax)    
      salida = False
      while(salida != True):
          for x in indice:
              if(x == randpos):
                  salida = True
                  return randpos 
          if(len(indice) == 1):
              salida = True
              return indice[0]
          randpos = random.randint(1,numMax) 
          
##############################################################################

def enter_move(board, indice, orden):
    #funcion para que el usario introduzca su movimiento
    indiceboard = indice
    print('Posiciones disponibles: ' + str(indiceboard))
    ultima_pos = len(indiceboard)-1
    comienza = orden[ultima_pos]
    orden.pop(len(indiceboard)-1)
    if comienza == 0:
        print('Comienza el jugador')
        print('Posicion:')
        posicion = int(input())
        contpos = 0
        for x in range(0, 3):
            for y in range(0, 3):
                contpos += 1
                if(contpos == posicion): 
                    board[x][y] = 'X'
        indiceboard.remove(posicion)
        return board
    if comienza == 1:
        print('Comienza el PC')
        numMax = 9
        randpos = chequeo_valor_pc(indiceboard, numMax)
        print(randpos)
        contpos = 1
        for x in range(0, 3):
            for y in range(0, 3):
              if(contpos == randpos): 
                board[x][y] = '0'
              contpos += 1
        indiceboard.remove(randpos)     
        return board
          
# Funcion de victoria (Finales del juego)
def victory_for(board, sign, indice):
    tabla = board
    # Casos para las X: diagonal-izq
    if((tabla[0][0] == 'X') and (tabla[1][1] == 'X') and (tabla[2][2] == 'X')):
        print('Gano la X')
        return True
    # Casos para las X: diagonal-der
    if((tabla[0][2] == 'X') and (tabla[1][1] == 'X') and (tabla[2][0] == 'X')):
        print('Gano la X')
        return True
    # Casos para las X: fila 1
    if((tabla[0][0] == 'X') and (tabla[1][0] == 'X') and (tabla[2][0] == 'X')):
        print('Gano la X')
        return True 
    # Casos para las X: fila 2
    if((tabla[0][1] == 'X') and (tabla[1][1] == 'X') and (tabla[2][1] == 'X')):
        print('Gano la X')
        return True 
    # Casos para las X: fila 3
    if((tabla[0][2] == 'X') and (tabla[1][2] == 'X') and (tabla[2][2] == 'X')):
        print('Gano la X')
        return True 
    # Casos para las X: columna 1
    if((tabla[0][0] == 'X') and (tabla[0][1] == 'X') and (tabla[0][2] == 'X')):
        print('Gano la X')
        return True  
    # Casos para las X: columna 2
    if((tabla[1][0] == 'X') and (tabla[1][1] == 'X') and (tabla[1][2] == 'X')):
        print('Gano la X')
        return True 
    # Casos para las X: columna 3
    if((tabla[2][0] == 'X') and (tabla[2][1] == 'X') and (tabla[2][2] == 'X')):
        print('Gano la X')
        return True   
    # Ahora el 0 
    # Casos para las 0: diagonal-izq
    if((tabla[0][0] == '0') and (tabla[1][1] == '0') and (tabla[2][2] == '0')):
        print('Gano la 0')
        return True
    # Casos para las X: diagonal-der
    if((tabla[0][2] == '0') and (tabla[1][1] == '0') and (tabla[2][0] == '0')):
        print('Gano la 0')
        return True
    # Casos para las X: fila 1
    if((tabla[0][0] == '0') and (tabla[1][0] == '0') and (tabla[2][0] == '0')):
        print('Gano la 0')
        return True 
    # Casos para las X: fila 2
    if((tabla[0][1] == '0') and (tabla[1][1] == '0') and (tabla[2][1] == '0')):
        print('Gano la 0')
        return True 
    # Casos para las X: fila 3
    if((tabla[0][2] == '0') and (tabla[1][2] == '0') and (tabla[2][2] == '0')):
        print('Gano la 0')
        return True    
    # Casos para las 0: columna 1
    if((tabla[0][0] == '0') and (tabla[0][1] == '0') and (tabla[0][2] == '0')):
        print('Gano la 0')
        return True  
    # Casos para las 0: columna 2
    if((tabla[1][0] == '0') and (tabla[1][1] == '0') and (tabla[1][2] == '0')):
        print('Gano la 0')
        return True 
    # Casos para las 0: columna 3
    if((tabla[2][0] == '0') and (tabla[2][1] == '0') and (tabla[2][2] == '0')):
        print('Gano la 0')
        return True
    # Caso de la casa 
    if(len(indice) == 0):
        print('Nadie a ganado. Empate. Gano la casa')
        return True
    return False

#Funcion de inicio
def jugar():
  #TODO inicializacion del juego
  tablero = [[" " for c in range(3)] for d in range(3)]
  indice = [1,2,3,4,5,6,7,8,9]
  orden = comienzo_de_turno(indice)
  fin = False
  print("Vamos a jugar al 3 en raya!!!")
  meta = False
  while(meta != True):
    meta = victory_for(tablero, fin, indice)
    if(meta != True):
        tablero = enter_move(tablero, indice, orden)
        display_board(tablero)
    else:
        print("Fin del Juego")
    
    
jugar()
