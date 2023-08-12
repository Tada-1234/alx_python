def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_sub_matrix = []
        for element in row:
            new_sub_matrix.append(element * element)
        new_matrix.append(new_sub_matrix)
    return new_matrix
