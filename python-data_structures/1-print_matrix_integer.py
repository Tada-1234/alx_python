#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if isinstance(matrix, list):
        count = 0
        for row in matrix:
           for element in row:
               if element == matrix[count][-1]:
                   print("{:d}".format(element), end="")
               else:
                   print("{:d}".format(element), end=" ")
           print("")
           count = count + 1
    else:
        print("{:}".format(matrix))
