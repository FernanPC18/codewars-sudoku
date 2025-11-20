def comprobar_columna(sudoku):

    numero_columnas = len(sudoku)

    columna = 0
    while columna < numero_columnas:

        lista_elementos_columna = []

        columna_index = 0
        while columna_index < numero_columnas:

            lista_elementos_columna += [sudoku[columna_index][columna]]

            if lista_elementos_columna.count(sudoku[columna_index][columna]) > 1:

                return False

            columna_index += 1

        columna += 1

    return True
  

if __name__ == '__main__':

    import sys
    sys.path.append('..')

    import casos_tests.casos_test_sudoku as casos_test

    assert comprobar_columna (casos_test.correcto)
    assert not comprobar_columna (casos_test.columna_invalida)
