def fibonancci(n):
    if(n==1 or n==2):
        return 1
    else:
        return fibonancci(n-1)+fibonancci(n-2)
print(fibonancci(12))
n=int(input("nhap n:"))
for i in range(1,n+1,1):
    print(fibonancci(i),end="   ")