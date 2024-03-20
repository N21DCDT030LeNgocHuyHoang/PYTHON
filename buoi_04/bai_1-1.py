def dao(array):
    start = 0
    end = len(array) - 1
    
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
My_List= [10,9,8,7,6,5,4,3,2,1,0]
dao(My_List)
print(My_List)  