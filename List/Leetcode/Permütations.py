def rotate_matrix(matrix):
    new = []
    matrix.reverse()
    for row in zip(*matrix):
        new.append(row)

    print(new)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate_matrix(matrix)
