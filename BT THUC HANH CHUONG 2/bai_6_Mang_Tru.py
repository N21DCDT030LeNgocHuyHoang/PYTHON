def Tru(a, b):
    n = len(a)
    m = len(b)
    
    # Xác định độ dài của danh sách kết quả
    maxLength = n
    result = [0] * maxLength
    
    borrow = 0 # Mượn khi trừ
    
    # Thực hiện phép trừ từ phải sang trái
    for i in range(maxLength):
        digitA = a[n - i - 1] if i < n else 0 # Lấy chữ số ở vị trí tương ứng của a, nếu không tồn tại thì lấy 0
        digitB = b[m - i - 1] if i < m else 0 # Lấy chữ số ở vị trí tương ứng của b, nếu không tồn tại thì lấy 0
        
        # Trừ đi số mượn
        digitA -= borrow
        
        # Nếu digitA nhỏ hơn digitB, mượn 1 từ chữ số cao hơn của a
        if digitA < digitB:
            digitA += 10
            borrow = 1
        else:
            borrow = 0
        
        # Tính hiệu
        diff = digitA - digitB
        
        result[maxLength - i - 1] = diff # Lưu kết quả vào danh sách kết quả
    
    return result

# Hàm main để kiểm tra
def main():
    a = [3, 2, 1] # Số 321
    b = [1] # Số 1
    
    result = Tru(a, b)
    
    print("Result:", result)

if __name__ == "__main__":
    main()
