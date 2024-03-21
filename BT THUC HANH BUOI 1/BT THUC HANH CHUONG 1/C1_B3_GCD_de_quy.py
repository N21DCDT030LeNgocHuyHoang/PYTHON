def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)
x = int(input("enter x:"))
y = int(input("enter y:"))
print("Ước số chung lớn nhất là: ")
print(gcd(x,y))