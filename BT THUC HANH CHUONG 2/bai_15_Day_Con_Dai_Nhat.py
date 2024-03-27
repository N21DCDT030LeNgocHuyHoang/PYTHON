def DayConDaiNhat(a, b):
    n = len(a)
    m = len(b)
    
    max_length = 0
    max_subarray = []
    
    for i in range(n):
        for j in range(m):
            length = 0
            subarray = []
            # Duyệt từng phần tử của a và b từ vị trí hiện tại
            while i + length < n and j + length < m and a[i + length] == b[j + length]:
                subarray.append(a[i + length])
                length += 1
                
            # Nếu độ dài của dãy con hiện tại lớn hơn dãy con dài nhất đã tìm thấy trước đó
            if length > max_length:
                max_length = length
                max_subarray = subarray
                
    return max_subarray

# Hàm main để kiểm tra
def main():
    a = [1, 6, 2, 5, 3, 7, 9, 4, 2, 8, 1, 5]
    b = [6, 2, 5, 3, 7, 9, 8, 1, 5]
    
    result = DayConDaiNhat(a, b)
    
    if result:
        print("Result:", result)
    else:
        print("Không tìm thấy dãy con chung.")

if __name__ == "__main__":
    main()
