def luyThua(x,n):
    if n==0:
        return 1
    else:
        return x* luyThua(x,n-1)
print(luyThua(2,4))