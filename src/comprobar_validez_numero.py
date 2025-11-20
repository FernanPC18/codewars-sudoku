def comprobar_validez_numero(sudoku):

    MAX_RANGE = len(sudoku) + 1
    numero_filas = len(sudoku)

    fila = 0
    while fila < numero_filas:

        columna = 0
        while columna < numero_filas:

            if sudoku[fila][columna] not in range (1, MAX_RANGE):

                return False
            
            columna += 1

        fila += 1
            
    return True


if __name__ == '__main__':

    import sys
    sys.path.append('..')

    import casos_tests.casos_test_sudoku as casos_test

    assert comprobar_validez_numero (casos_test.correcto)
    assert comprobar_validez_numero (casos_test.columna_invalida)
    assert not comprobar_validez_numero (casos_test.no_entero)
    assert not comprobar_validez_numero (casos_test.no_cuadrado)
    assert not comprobar_validez_numero (casos_test.rango_sobrepasado)