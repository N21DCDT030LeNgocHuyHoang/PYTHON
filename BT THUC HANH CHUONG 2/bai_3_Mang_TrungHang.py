def Mang_TrungHang(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Kiểm tra xem ma trận có là ma trận vuông không
    if num_rows != num_cols:
        return False
def Mang_TrungHang(matrix):
    num_rows = len(matrix)
    row_set = set()

    for row in matrix:
        row_tuple = tuple(row)
        if row_tuple in row_set:
            return True
        else:
            row_set.add(row_tuple)  
    return False  
matrix1 = [
    [1, 2, 3],
    [1, 2, 3],
    [7, 8, 7]
]

matrix2 = [
    [1, 2, 5],
    [4, 5, 4],
    [1, 2, 3]
]
if Mang_TrungHang(matrix1):
    print("Ma trận 1 có ít nhất hai hàng giống nhau")
else:
    print("Ma trận 1 không có hàng giống nhau")

if Mang_TrungHang(matrix2):
    print("Ma trận 2 có ít nhất hai hàng giống nhau")
else:
    print("Ma trận 2 không có hàng giống nhau")
