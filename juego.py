def crea_tablero(fila, columna):
    salida =[]
    for element in range(columna):
        lista2 = []
        for i in range(fila):
            lista2.append(0)
        salida.append(lista2)
    return salida

def juega(columna, jugador):
    '''
    Ver si la columna tiene hueco
    Si lo tiene en ese hueco poner la ficha jugador
    '''

def busca_hueco(columna):
    '''
    Buscar la ultima posicion vacía de la columna del tablero
    '''                 