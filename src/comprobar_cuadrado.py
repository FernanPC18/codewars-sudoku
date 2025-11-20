def comprobar_cuadrado(sudoku):

    numero_filas = len(sudoku)

    fila = 0
    while fila < numero_filas:

        if len(sudoku[fila]) != numero_filas:

            return False
        
        else:

            fila += 1

    return True

if __name__ == '__main__':


    import sys
    sys.path.append('..')

    import casos_tests.casos_test_sudoku as casos_test

    assert comprobar_cuadrado (casos_test.correcto)
    assert not comprobar_cuadrado (casos_test.no_cuadrado)
    assert not comprobar_cuadrado (casos_test.no_numeros)