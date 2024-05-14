def Hop(arr_a, arr_b):
    set_a = set(arr_a)
    set_b = set(arr_b)

    union_set = sorted(set_a.union(set_b))
    return union_set

arr_a = [1, 5, 3, 7, 9, 4, 2]
arr_b = [9, 6, 2, 3, 8]
result = Hop(arr_a, arr_b)
print(result)
