def Tru(a, b):
    # Hàm kiểm tra xem số a có phải là số âm không
    def is_negative(num):
        return num[0] == 1
    
    # Hàm để đảo dấu của số
    def negate(num):
        num[0] = 1 - num[0]
    
    # Hàm để kiểm tra xem hai số có cùng dấu không
    def same_sign(num1, num2):
        return is_negative(num1) == is_negative(num2)
    
    # Hàm để cộng hai số nguyên không dấu
    def add_unsigned(num1, num2):
        result = []
        carry = 0
        len1, len2 = len(num1), len(num2)
        maxLength = max(len1, len2)
        
        # Thực hiện phép cộng từ phải sang trái
        for i in range(maxLength):
            digit1 = num1[len1 - i - 1] if i < len1 else 0
            digit2 = num2[len2 - i - 1] if i < len2 else 0
            
            total = digit1 + digit2 + carry
            result.insert(0, total % 10)
            carry = total // 10
        
        if carry > 0:
            result.insert(0, carry)
        
        return result
    
    # Kiểm tra trường hợp đặc biệt nếu một trong hai số là 0
    if b[0] == 0:
        return a
    elif a[0] == 0:
        result = b.copy()
        negate(result)
        return result
    
    # Kiểm tra xem hai số có cùng dấu không
    if same_sign(a, b):
        if is_negative(a):
            # Nếu a là số âm, thực hiện a - b
            if a > b:
                result = subtract_unsigned(a[1:], b[1:])
                return [1] + result if result != [0] else result
            else:
                result = subtract_unsigned(b[1:], a[1:])
                return result if result != [0] else result
        else:
            # Nếu a là số dương, thực hiện a - b
            if a > b:
                return subtract_unsigned(a[1:], b[1:])
            else:
                result = subtract_unsigned(b[1:], a[1:])
                return [1] + result if result != [0] else result
    else:
        # Nếu hai số có dấu khác nhau, thực hiện phép cộng của hai số tuyệt đối
        if is_negative(a):
            negate(a)
            result = add_unsigned(a[1:], b[1:])
            return result
        else:
            negate(b)
            result = add_unsigned(a[1:], b[1:])
            return result if result != [0] else result

# Hàm để trừ hai số nguyên không dấu
def subtract_unsigned(num1, num2):
    result = []
    borrow = 0
    len1, len2 = len(num1), len(num2)
    maxLength = max(len1, len2)
    
    # Thực hiện phép trừ từ phải sang trái
    for i in range(maxLength):
        digit1 = num1[len1 - i - 1] if i < len1 else 0
        digit2 = num2[len2 - i - 1] if i < len2 else 0
        
        # Trừ đi số mượn
        digit1 -= borrow
        
        # Nếu digit1 nhỏ hơn digit2, mượn 1 từ chữ số cao hơn của num1
        if digit1 < digit2:
            digit1 += 10
            borrow = 1
        else:
            borrow = 0
        
        # Tính hiệu
        diff = digit1 - digit2
        
        result.insert(0, diff)  # Lưu kết quả vào danh sách kết quả
    
    # Loại bỏ các số 0 thừa ở đầu
    while len(result) > 1 and result[0] == 0:
        result.pop(0)
    
    return result

# Hàm main để kiểm tra
def main():
    a = [0, 1, 2, 3]  # Số 123
    b = [1, 4, 5, 6]  # Số -456
    
    result = Tru(a, b)
    
    if result == [-1]:
        print("Overflow")
    else:
        print("Result:", result)

if __name__ == "__main__":
    main()
