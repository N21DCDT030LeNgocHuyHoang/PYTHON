def TrungCot(matrix):
    n = len(matrix)
    
    # Kiểm tra từng cột
    for j in range(n):
        # Tạo một tập hợp để lưu trữ giá trị của cột j
        col_values = set()
        
        # Lặp qua từng hàng trong cột j
        for i in range(n):
            col_values.add(matrix[i][j])
        
        # Kiểm tra xem có cột nào có giống nhau không
        if len(col_values) != n:  # Nếu kích thước tập hợp nhỏ hơn kích thước của ma trận
            return True
    
    return False

# Hàm main để kiểm tra
def main():
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Matrix 1:", TrungCot(matrix1))  # False
    
    matrix2 = [
        [1, 2, 3],
        [4, 2, 6],
        [7, 2, 9]
    ]
    print("Matrix 2:", TrungCot(matrix2))  # True

if __name__ == "__main__":
    main()
