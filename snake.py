def board(x:int , y:int):
    field = [['*' for contx in range(x)] for conty in range(y)]
    fieldBackup = [[contx for contx in range(x)] for conty in range(y)]
    print('Profundidad de la serpiente:')
    depth = int(input())
    snake = positionInitial(field, fieldBackup)
    positionEnd(field, fieldBackup)
    screen(field)
    followPosition(snake, depth, field, fieldBackup)

def positionEnd(field, fieldBackup):
    option = 0
    while(option != -1):
        try:
            print(field)
            print('Introduzca numero de posicion de meta en x:')
            r = int(input())
            print('Introudzca numero de posicion de meta en y:')
            c = int(input())    
            field[r][c] = 'F'
            option = -1
        except Exception:
            print('Numero equivocado intente de nuevo')

def positionInitial(field, fieldBackup):
    option = 0
    while(option != -1):
        try:
            snake = []
            print(field)
            print('Introduzca numero de posicion inicial en x:')
            r = int(input())
            print('Introudzca numero de posicion inicial en y:')
            c = int(input())
            field[r][c] = 'H'
            snake.append([r,c])
            fieldBackup[r].remove(c)
            option = -1        
        except Exception:
            print('Numero equivocado intente de nuevo')
    return snake        
        
def followCondition(snake, field, depth, fieldBackup, colPositionX, colPositionY):
    cont_depth = 1
    x = colPositionX
    y = colPositionY
    maps = field
    lenX = len(maps)
    lenY = len(maps[0])
    while(depth >= cont_depth):
        #Caso C: Si el final esta una posicion x+1 o y+1 del inicio
        #Posiciones iniciales
        value1 = snake[0][0]
        value2 = snake[0][1]

        if((maps[value1][value2].find('H') == 0) and (maps[value1-1][value2].find('F') == 0)):
            maps[x][y] = 'H'
            fieldBackup[x].remove(y)
            snake.append([x,y])
            if((maps[value1-1][y].find('*') == 0) and (maps[value1-1][y+1].find('F') == 0)):            
                maps[value1-1][y] = 'H'
                fieldBackup[value1-1].remove(y)
                snake.append([value1-1,y]) 
                break
        #Caso B: Si la profundidad excede del tamano indicado
        if(depth >= lenX*lenY):
            if(maps[x][y].find('*') == 0):
                 maps[x][y] = 'H'
                 fieldBackup[x].remove(y)
                 snake.append([x,y])
                 if(maps[x+1][y].find('*') == 0):
                     maps[x+1][y] = 'H'
                     fieldBackup[x+1].remove(y)  
            else:
                 maps[x][y] = 'H'
                 fieldBackup[x].remove(y)
                 snake.append([x,y])
                 
        
        #Caso A1: Si la posicion x e y son iguales y 
        #    si esta en la ultima posicion los dos intervalos  (x, y)
        if((lenX-1 == colPositionX) and (lenY-1 == colPositionY)):            
             if(maps[x][y].find('*') == 0):
                 maps[x][y] = 'H'
                 fieldBackup[x].remove(y)
                 snake.append([x,y])
                 # suba una posicion hacia arriba en la misma posicion y
                 x = x - 1
                 
        #Caso A2: complete las posiciones por el valor del fondo 
        if((lenX-1 != colPositionX) and (lenY-1 != colPositionY)): 
              if(maps[x][y].find('*') == 0):
                  maps[x][y] = 'H'
                  fieldBackup[x].remove(y)
                  snake.append([x,y])
                 
        # #Caso A2.1: si llegado a la meta aplique el caso A2    
              else:
                if(maps[x][y].find('F') == 0):
                    maps[x][y] = 'H'
                    fieldBackup[x].remove(y)
                    snake.append([x,y])
                    cont_depth = cont_depth + depth
                    
                y = y + 1
               
        cont_depth = cont_depth + 1   

def endGame(field):
    #Caso 1: si es igual a f  false
    #Caso 2: si no lo encuentra true
    maps = field
    value = 0
    for x in range(len(maps)):
        for y in range(len(maps[x])):
            if(maps[x][y].find('F') == 0):
                value = 1
    return value                           

def followPosition(snake, depth, field, fieldBackup):
    option = 0
    while(option == 0):        
        print('Posiciones Disponibles:' + str(fieldBackup))
        print('Snake:'+str(snake)+'\n')
        screen(field)
        try:
            if(endGame(field) == 0):
                print('Fin del juego')
                #print('Puntuacion:'+point_game(depth, fieldBackup))
                break
            else:                
                print('Introduzca valor a la siguiente posicion x:')
                r = int(input())
                print('Introudzca valor a la siguiente posicion y:')
                c = int(input())
    
                followCondition(snake,field, depth, fieldBackup, r, c)
                screen(field)
                print()

        except Exception:
            print(Exception().__str__())

def point_game(depth, fieldBackup):
    path_free = len(fieldBackup)
    if((1 <= depth) and (depth <= 20)):
        x = depth + 1
        y = 20 - x
        punt = path_free - depth
        if(punt < 1):
            punt = 1
        return punt

def screen(field):
    for contx in range(len(field)):
        for conty in range(len(field[contx])):
            print(field[contx][conty], end=' ')
        print()      
    print()
       

def main():
    print('Tamano de la matriz en x:')
    x = int(input())
    print('Tamano de la matriz en y:')
    y = int(input())
    board(x,y)

#numberOfAvailableDifferentPaths(board, snake, depth)
#r = int(input())
