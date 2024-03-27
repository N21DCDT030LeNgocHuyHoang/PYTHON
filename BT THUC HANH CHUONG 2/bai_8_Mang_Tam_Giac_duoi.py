def TamGiacDuoi(matrix):
    n = len(matrix)
    
    # Kiểm tra từng phần tử phía trên đường chéo chính
    for i in range(1, n):
        for j in range(i):
            if matrix[i][j] != 0:  # Nếu có phần tử khác không
                return False
    
    return True

# Hàm main để kiểm tra
def main():
    matrix1 = [
        [1, 0, 0],
        [2, 3, 0],
        [4, 5, 6]
    ]
    print("Matrix 1:", TamGiacDuoi(matrix1))  # True
    
    matrix2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Matrix 2:", TamGiacDuoi(matrix2))  # False

if __name__ == "__main__":
    main()
