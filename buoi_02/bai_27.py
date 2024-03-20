import numpy as np
twoDArray = np.array([11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9])
print(twoDArray)

def searchTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
           if array[i][j] == value:
               return 'The value is located at index'+str (i)+" "+ str(j)
    return'the element is not found'

print(searchTDArray(twoDArray,55))
# Time complexity O(mn)
# Space complexity O(1)