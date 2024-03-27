def DayConDauTien(a, b):
    n = len(a)
    m = len(b)
    
    result = []
    
    for i in range(n):
        for j in range(m):
            # Đảm bảo không vượt quá kích thước của cả hai mảng
            if i < n and j < m:
                # Nếu hai phần tử tại vị trí hiện tại của a và b giống nhau
                if a[i] == b[j]:
                    # Tạo một dãy con từ vị trí hiện tại và kiểm tra xem dãy con này có trong cả hai mảng không
                    temp_a = a[i:]
                    temp_b = b[j:]
                    
                    if temp_a == temp_b:
                        result = temp_a
                        return result
    return result

# Hàm main để kiểm tra
def main():
    a = [1, 6, 2, 5, 3, 7, 9, 4, 2]
    b = [9, 6, 2, 5, 3, 7, 8]
    
    result = DayConDauTien(a, b)
    
    if result:
        print("Result:", result)
    else:
        print("Không tìm thấy dãy con chung.")

if __name__ == "__main__":
    main()
