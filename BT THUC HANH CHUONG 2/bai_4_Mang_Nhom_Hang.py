def Mang_NhomHang(matrix):
    num_rows = len(matrix)

    # Dùng một dictionary để lưu trữ các hàng dưới dạng chuỗi và chỉ mục của chúng
    row_groups = {}

    # Duyệt qua từng hàng của ma trận
    for i in range(num_rows):
        # Chuyển đổi hàng thành chuỗi để so sánh
        row_string = str(matrix[i])

        # Nếu chuỗi hàng đã xuất hiện trong dictionary, thêm chỉ mục của hàng vào nhóm
        if row_string in row_groups:
            row_groups[row_string].append(i)
        else:
            # Nếu chuỗi hàng chưa xuất hiện, tạo một nhóm mới
            row_groups[row_string] = [i]

    # In ra các nhóm hàng giống nhau
    for group in row_groups.values():
        if len(group) > 1:  # Chỉ in nhóm nếu có ít nhất hai hàng trong nhóm
            print("Nhóm hàng:", group)

# Ví dụ sử dụng
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3],
    [7, 8, 9],
    [4, 5, 6]
]

print("Các nhóm hàng giống nhau:")
Mang_NhomHang(matrix)