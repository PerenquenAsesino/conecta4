from juego_functions import crea_tablero
from juego_functions import juega
from juego_functions import esta_llena
from juego_functions import victoria_vertical_col
from juego_functions import victoria
from juego_functions import victoria_horizontal_fila



def test_crear_tablero():
    tab = crea_tablero(4, 3)

    assert tab == [[0,0,0,0],[0,0,0,0], [0,0,0,0]]

def test_anyadir_ficha_a_tablero():
    tab = crea_tablero(4,3)
    juega(tab, 2, 1)

    assert tab == [[0,0,0,0],[0,0,0,0], [0,0,0,1]]

def test_comprobar_columna_llena():
    tab = crea_tablero(4, 3)
    juega(tab, 2, "x")
    juega(tab, 2, "x")
    juega(tab, 2, "x")
    juega(tab, 2, "x")

    assert esta_llena(tab, 2) == True

def test_victoria_vertical_columna():
    tab = crea_tablero(6, 7)
    assert victoria_vertical_col(tab, 2, "x") == False
    juega (tab, 2, "x")

def test_victoria_vertical_tablero():
    tab = crea_tablero(6, 7)

    assert victoria(tab, "x") == False
    juega(tab, 2, "x")
    juega(tab, 2, "o")
    juega(tab, 2, "x")
    juega(tab, 2, "x")
    juega(tab, 2, "x")
    juega(tab, 2, "x")

    assert victoria(tab, "x") 
    assert victoria(tab, "o") == False

def test_victoria_horizontal_fila():
    tab = crea_tablero(6, 7)
    juega(tab, 0, "x")
    juega(tab, 1, "o")
    juega(tab, 2, "x")
    juega(tab, 3, "x")
    juega(tab, 4, "x")
    juega(tab, 5, "x")

    assert victoria_horizontal_fila(tab, 5, "x")

def test_victoria_horizontal_tablero():
    tab = crea_tablero(6, 7)
    juega(tab, 0, "x")
    juega(tab, 1, "o")
    juega(tab, 2, "x")
    juega(tab, 3, "x")
    juega(tab, 4, "x")
    juega(tab, 5, "x")

    assert victoria(tab, "x") == True
    assert victoria(tab, "o") == False
