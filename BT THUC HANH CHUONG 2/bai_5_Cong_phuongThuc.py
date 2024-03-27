def Cong(a, b):
    n = len(a)
    m = len(b)
    
    # Xác định độ dài của mảng kết quả
    maxLength = max(n, m)
    result = [0] * (maxLength + 1)  # Mảng kết quả có thể lớn hơn một chút nếu có carry
    
    carry = 0  # Biến nhớ khi cộng
    
    # Thực hiện cộng từ phải sang trái
    for i in range(maxLength):
        digitA = a[n - i - 1] if i < n else 0  # Lấy chữ số ở vị trí tương ứng của a, nếu không tồn tại thì lấy 0
        digitB = b[m - i - 1] if i < m else 0  # Lấy chữ số ở vị trí tương ứng của b, nếu không tồn tại thì lấy 0
        
        # Tính tổng
        total = digitA + digitB + carry
        
        # Kiểm tra có carry không
        if total > 9:
            carry = 1
            total -= 10
        else:
            carry = 0
        
        # Lưu kết quả vào mảng kết quả
        result[maxLength - i] = total
    
    # Nếu có carry cuối cùng thì mảng kết quả bị tràn
    if carry == 1:
        return [-1] * (maxLength + 1)
    else:
        return result[1:]  # Loại bỏ phần tử thừa ở đầu (carry)

# Hàm main để kiểm tra
def main():
    a = [1, 2, 3]  # Số 123
    b = [4, 5, 6]  # Số 456
    
    result = Cong(a, b)
    
    if result[0] == -1:
        print("Overflow")
    else:
        print("Result:", result)

if __name__ == "__main__":
    main()
