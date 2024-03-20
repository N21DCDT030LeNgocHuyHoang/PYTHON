def Giai(n):
    if n==0:
        return 1
    else:
        return n * Giai(n-1)
a=Giai(5)
print(a)