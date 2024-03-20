def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            # top <- left
            matrix[first][i] = matrix[last - offset][first]
            # left <- bottom
            matrix[last - offset][first] = matrix[last][last - offset]
            # bottom <- right
            matrix[last][last - offset] = matrix[i][last]
            # right <- top
            matrix[i][last] = top
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_matrix(matrix)
print(matrix)