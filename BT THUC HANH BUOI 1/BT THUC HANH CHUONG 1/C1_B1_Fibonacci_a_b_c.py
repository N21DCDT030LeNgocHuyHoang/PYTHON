#Giải thuật không đệ qui: dùng ba biến a, b, c để lưu ba số Fibonacci kế tiếp nhau.
def fibonacci_non_recursive(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        c = a + b
        a, b = b, c
    return b


n = int(input("Nhập vào số nguyên n: "))
if n < 0:
    print("n phải lớn hơn hoặc bằng 0.")
else:
    result_non_recursive = fibonacci_non_recursive(n)
    print("Số Fibonacci thứ", n, "không sử dụng đệ qui là:", result_non_recursive)

