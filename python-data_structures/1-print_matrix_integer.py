def print_matrix_integer(matrix=[[]]):
    if isinstance(matrix, list):
        for row in matrix:
            print(" ".join(map(str, row)))
    else:
        print("{:}".format(matrix))
