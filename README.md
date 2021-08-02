# Python
Es un lenguaje de programacion orientado a objetos, con una alta semantica dinamica que permite estructurar, la construccion de datos estructurales y no estructurales.

# Snake.py

# Condiciones del programa:
        Caso C: Si el final esta una posicion x+1 o y+1 del inicio
        Posiciones iniciales
        Caso B: Si la profundidad excede del tamano indicado
        Caso A1: Si la posicion x e y son iguales y si esta en la ultima posicion, los dos intervalos  (x, y)
            * baja una posicion x en la misma posicion y 
        Caso A2: completa las posiciones por el valor del fondo 
        Caso A2.1: si llegado a la meta aplique el caso A2  
        

# Test 1: 
        board: [4, 3] 
        snake: [[2,2],  [3,2],  [3,1],  [3,0],  [2,0],  [1,0],  [0,0]] 
        depth: 3 
        Result: 7 
 
# Test 2: 
        board: [2, 3] 
        snake: [[0,2],  [0,1],  [0,0],  [1,0],  [1,1],  [1,2]] 
        depth: 10 
        Result: 1 
 
# Test 3: 
        board: [10, 10] 
        ○snake: [[5,5],  [5,4],  [4,4],  [4,5]] 
        ○depth: 4 
        Result: 81
