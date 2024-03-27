def Mang_TamGiacTren(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Kiểm tra xem ma trận có là ma trận vuông không
    if num_rows != num_cols:
        return False

    # Kiểm tra các phần tử nằm dưới hoặc trên đường chéo chính có bằng 0 hay không
    for i in range(num_rows):
        for j in range(num_cols):
            # Kiểm tra các phần tử nằm trên đường chéo chính hoặc bên dưới nó
            if i > j and matrix[i][j] != 0:
                return False
    return True


matrix1 = [
    [1, 2, 3],
    [0, 4, 5],
    [0, 0, 6]
]
if Mang_TamGiacTren(matrix1):
    print("Ma trận 1 là ma trận tam giác trên.")
else:
    print("Ma trận 1 không phải là ma trận tam giác trên.")
