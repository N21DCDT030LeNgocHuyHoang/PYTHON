def Cong(a, b):
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
    if a[0] == 0:
        return b
    elif b[0] == 0:
        return a
    
    # Kiểm tra xem hai số có cùng dấu không
    if same_sign(a, b):
        result = add_unsigned(a[1:], b[1:])
        return [a[0]] + result if is_negative(a) else result
    else:
        # Trường hợp hai số có dấu khác nhau
        if is_negative(a):  # Nếu a là số âm
            negate(a)  # Đảo dấu của a
            if a > b:  # Nếu giá trị tuyệt đối của a lớn hơn b, trả về kết quả sau khi trừ
                result = Tru(a, b)
                return result
            else:  # Ngược lại, trả về kết quả sau khi trừ với dấu đảo của kết quả
                result = Tru(b, a)
                negate(result)
                return result
        else:  # Nếu b là số âm, thực hiện tương tự như trên
            negate(b)
            if a > b:
                result = Tru(a, b)
                return result
            else:
                result = Tru(b, a)
                negate(result)
                return result

# Hàm main để kiểm tra
def main():
    a = [0, 1, 2, 3]  # Số 123
    b = [1, 4, 5, 6]  # Số -456
    
    result = Cong(a, b)
    
    if result == [-1]:
        print("Overflow")
    else:
        print("Result:", result)

if __name__ == "__main__":
    main()
