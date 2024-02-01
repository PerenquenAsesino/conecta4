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