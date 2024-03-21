import numpy as np
n = int(input("Nhập n: "))
pascal = np.zeros((n, n),dtype=int)
pascal[0][0] = 1

for i in range(1, n):
    pascal[i][0] =1
    pascal[i][i] =1
    for j in range(1, i):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

for i in range(n):
    for j in range(i+1):
        print(pascal[i][j], end=" ")
    print()
