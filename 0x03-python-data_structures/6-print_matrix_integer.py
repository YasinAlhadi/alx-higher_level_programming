#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        print()
    else:
        for i in range(0, len(matrix)):
            for x in range(0, len(matrix[i])):
                if x != len(matrix[i]) - 1:
                    print('{:d} '.format(matrix[i][x]), end='')
                else:
                    print('{:d}'.format(matrix[i][x]))
