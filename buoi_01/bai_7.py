def sumOfDigits(n):
    if n==0:
        return 0
    if n<0 or not isinstance(n,int):
        raise("is integer ")
    else:
        return n % 10 + sumOfDigits(n//10)
print(sumOfDigits(1114))
