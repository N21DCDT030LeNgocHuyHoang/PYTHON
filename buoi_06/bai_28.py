def tong_hai_tuple(tuple1, tuple2):
    if not tuple1: 
        return sum(tuple2)
    if not tuple2:  
        return sum(tuple1)
    return tuple1[0] + tuple2[0] + tong_hai_tuple(tuple1[1:], tuple2[1:])

tuple1 = (1, 2, 3)
tuple2 = (5, 7, 9)
tong = tong_hai_tuple(tuple1, tuple2)
print("Tổng của hai tuple là:", tong)