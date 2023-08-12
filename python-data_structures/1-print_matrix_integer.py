def print_matrix_integer(matrix=[[]]):
    if isinstance(matrix, list):
        for row in matrix:
           formatted_row = " ".join("{:1}".format(value) for value in row)
           print(formatted_row)
    else:
        print("{:}".format(matrix))
