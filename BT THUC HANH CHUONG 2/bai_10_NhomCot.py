def NhomCot(matrix):
    n = len(matrix)
    
    # Tạo một từ điển để lưu trữ chỉ mục cột của các giá trị cột giống nhau
    column_groups = {}
    
    # Kiểm tra từng cột
    for j in range(n):
        # Tạo một chuỗi để lưu trữ chỉ mục của các cột giống nhau
        column_group_str = ''
        
        # Kiểm tra xem cột j có giống với các cột trước đó không
        for prev_j in range(j):
            if all(matrix[i][prev_j] == matrix[i][j] for i in range(n)):
                column_group_str += str(prev_j) + ', '
        
        # Nếu chuỗi không rỗng, đóng gói chuỗi vào từ điển
        if column_group_str:
            column_group_str += str(j)  # Thêm chỉ mục của cột hiện tại vào chuỗi
            column_groups[j] = column_group_str
    
    # In ra các nhóm chỉ mục cột
    for group in column_groups.values():
        print("Group:", group)

# Hàm main để kiểm tra
def main():
    matrix = [
        [1, 2, 3, 1],
        [4, 2, 6, 2],
        [7, 2, 9, 1],
        [1, 2, 3, 1]
    ]
    
    NhomCot(matrix)

if __name__ == "__main__":
    main()
