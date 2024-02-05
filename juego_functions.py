def crea_tablero(fila, columna):
    salida =[]
    for element in range(columna):
        lista2 = []
        for i in range(fila):
            lista2.append(0)
        salida.append(lista2)
    return salida

def juega(tablero, columna, valor_ficha):
    c = tablero[columna]
    indice = len(c)-1
    while indice < len(c):
        if c[indice] == 0:
            c[indice] = valor_ficha
            break
        indice -= 1

def esta_llena(tablero, columna):
    c = tablero[columna]
    return 0 not in c

def victoria_vertical_col(tablero, pos_columna, ficha):
    contador_iguales = 0
    columna = tablero[pos_columna]

    ix = 0
    while ix < len(columna):
        if columna[ix] == ficha:
            contador_iguales += 1
        else:
            contador_iguales = 0
              
        ix += 1
        if contador_iguales == 4:
            return True
        
    return False

def victoria(tablero, ficha):
    num_cols = len(tablero)
    for num_col in range(num_cols):
        if victoria_vertical_col(tablero, num_col, ficha):
            return True
    
    num_filas = len(tablero[0])
    for num_fila in range(num_filas):
        if victoria_horizontal_fila(tablero, num_fila, ficha):
            return True

    return False

def victoria_horizontal_fila(tablero, pos_fila, ficha):
    contador_iguales = 0

    for columna in tablero:
        if columna[pos_fila] == ficha:
            contador_iguales += 1
        else:
            contador_iguales = 0

        if contador_iguales == 4:
            return True
    return False
        