def crea_tablero(fila, columna):
    salida =[]
    for element in range(columna):
        lista2 = []
        for i in range(fila):
            lista2.append(0)
        salida.append(lista2)
    return salida