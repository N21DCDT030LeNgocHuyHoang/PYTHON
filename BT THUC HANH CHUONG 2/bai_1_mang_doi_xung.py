def Mang_DoiXung(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    if num_rows != num_cols:
        return False
    
    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def nhap_ma_tran():
    # Nhập số hàng và số cột của ma trận
    num_rows = int(input("Nhập số hàng của ma trận: "))
    num_cols = int(input("Nhập số cột của ma trận: "))

    matrix = []

    # Nhập giá trị cho từng phần tử của ma trận
    print("Nhập giá trị cho từng phần tử của ma trận:")
    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            element = int(input("Nhập giá trị cho phần tử ({}, {}): ".format(i, j)))
            row.append(element)
        matrix.append(row)

    return matrix

def main():
    matrix = nhap_ma_tran()

    # Kiểm tra xem ma trận có là ma trận đối xứng không
    if Mang_DoiXung(matrix):
        print("Ma trận là ma trận đối xứng.")
    else:
        print("Ma trận không phải là ma trận đối xứng.")


