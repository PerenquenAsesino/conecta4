from juego_functions import crea_tablero
from juego_functions import juega

def test_crear_tablero():
    tab = crea_tablero(4, 3)

    assert tab == [[0,0,0,0],[0,0,0,0], [0,0,0,0]]

def test_anyadir_ficha_a_tablero():
    tab = crea_tablero(4,3)
    juega(tab, 2, 1)

    assert tab == [[0,0,0,0],[0,0,0,0], [0,0,0,1]]