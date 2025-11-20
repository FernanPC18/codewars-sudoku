def comprobar_fila(sudoku):

    numero_filas = len(sudoku)

    fila = 0
    while fila < numero_filas:

        fila_index = 0

        while fila_index < numero_filas:

            if sudoku[fila].count(sudoku[fila][fila_index]) > 1:

                return False
            
            fila_index += 1

        fila += 1

    return True


if __name__ == '__main__':

    import sys
    sys.path.append('..')

    import casos_tests.casos_test_sudoku as casos_test

    assert comprobar_fila (casos_test.correcto)
    assert not comprobar_fila (casos_test.fila_invalida)