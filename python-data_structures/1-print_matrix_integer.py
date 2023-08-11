def print_matrix_integer(matrix=[[]]):
    if isinstance(matrix, list):
        for row in matrix:
            for element in row:
                 print("{:d}".format(element), end=" ")
            print("",end="$\n")
    else:
        print("{:}$".format(matrix))
