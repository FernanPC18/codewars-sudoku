
if __name__ != '__main__':
    import sys
    sys.path.append('src')

from comprobar_columna import comprobar_columna
from comprobar_fila import comprobar_fila
from comprobar_cuadrado import comprobar_cuadrado
from comprobar_validez_numero import comprobar_validez_numero


def check_sudoku(sudoku):

    return comprobar_cuadrado(sudoku) and comprobar_validez_numero(sudoku) and comprobar_fila(sudoku) and comprobar_columna(sudoku)


if __name__ == '__main__':

    import sys
    sys.path.append('..')

    import casos_tests.casos_test_sudoku as casos_test

    assert check_sudoku (casos_test.correcto)
    assert not check_sudoku (casos_test.columna_invalida)
    assert not check_sudoku (casos_test.fila_invalida)
    assert not check_sudoku (casos_test.no_cuadrado)
    assert not check_sudoku (casos_test.no_entero)
    assert not check_sudoku (casos_test.no_numeros)
    assert not check_sudoku (casos_test.lista_vacia)
    assert not check_sudoku (casos_test.rango_sobrepasado)