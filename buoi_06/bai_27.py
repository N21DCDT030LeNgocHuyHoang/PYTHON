def tinh_tong_tich(tuple1):
    tong = sum(tuple1)
    tich = 1
    for i in tuple1:
        tich *= i  # Đổi từ i * (i+1) thành tich *= i
    return tong, tich  # Trả về cả tổng và tích trong tuple

my_tuple = (1, 2, 3, 4)
tong, tich = tinh_tong_tich(my_tuple)
print("Tổng của các phần tử trong tuple:", tong)
print("Tích của các phần tử trong tuple:", tich)
