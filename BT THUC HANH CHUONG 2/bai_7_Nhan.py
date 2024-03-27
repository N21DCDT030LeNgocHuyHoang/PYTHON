def Nhan(a, b):
    n = len(a)
    m = len(b)
    
    # Xác định độ dài của mảng kết quả
    maxLength = n + m
    result = [0] * maxLength
    
    # Thực hiện phép nhân từ phải sang trái
    for i in range(n-1, -1, -1):
        carry = 0  # Biến nhớ khi nhân
        
        for j in range(m-1, -1, -1):
            # Nhân từng chữ số của a với từng chữ số của b, và cộng vào vị trí tương ứng trong mảng kết quả
            product = a[i] * b[j] + result[i + j + 1] + carry
            result[i + j + 1] = product % 10
            carry = product // 10
        
        # Lưu giá trị carry nếu cần
        result[i + j] += carry
    
    # Kiểm tra xem kết quả có bị tràn không
    if result[0] == 0:
        return result[1:]
    else:
        return [-1] * maxLength

# Hàm main để kiểm tra
def main():
    a = [1, 2, 3]  # Số 123
    b = [4, 5, 6]  # Số 456
    
    result = Nhan(a, b)
    
    if result[0] == -1:
        print("Overflow")
    else:
        print("Result:", result)

if __name__ == "__main__":
    main()
