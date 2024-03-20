def reverse_integer(n, reverse_number=0):
    if n == 0:
        return reverse_number
    last_digit = n % 10
    reverse_number = reverse_number * 10 + last_digit
    return reverse_integer(n // 10, reverse_number)
number = 78965

reverse_number = reverse_integer(number)
print( reverse_number)  
