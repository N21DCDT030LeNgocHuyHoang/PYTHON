def Nhan(a, b):
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
    if a[0] == 0 or b[0] == 0:
        return [0]
    
    # Kiểm tra xem hai số có cùng dấu không
    if same_sign(a, b):
        result = multiply_unsigned(a[1:], b[1:])
        return [0] + result if is_negative(a) else result
    else:
        # Nếu hai số có dấu khác nhau, kết quả sẽ là số âm
        negate(a)
        negate(b)
        result = multiply_unsigned(a[1:], b[1:])
        return result

# Hàm để nhân hai số nguyên không dấu
def multiply_unsigned(num1, num2):
    len1, len2 = len(num1), len(num2)
    result = [0] * (len1 + len2)
    
    # Thực hiện phép nhân từ phải sang trái
    for i in range(len1-1, -1, -1):
        carry = 0
        digit1 = num1[i]
        
        for j in range(len2-1, -1, -1):
            digit2 = num2[j]
            product = digit1 * digit2 + result[i + j + 1] + carry
            result[i + j + 1] = product % 10
            carry = product // 10
        
        result[i] += carry
    
    # Loại bỏ các số 0 thừa ở đầu
    while len(result) > 1 and result[0] == 0:
        result.pop(0)
    
    return result

# Hàm main để kiểm tra
def main():
    a = [0, 1, 2, 3]  # Số 123
    b = [1, 4, 5, 6]  # Số -456
    
    result = Nhan(a, b)
    
    if result == [-1]:
        print("Overflow")
    else:
        print("Result:", result)

if __name__ == "__main__":
    main()
