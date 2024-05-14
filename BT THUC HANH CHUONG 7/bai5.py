class DoThi:
    def __init__(self, so_dinh):
        self.so_dinh = so_dinh
        self.dinh_ke = [[] for _ in range(so_dinh)]

    def them_canh(self, u, v):
        self.dinh_ke[u].append(v)
        self.dinh_ke[v].append(u)  # Vì là đồ thị vô hướng, nên ta thêm cạnh ở cả hai chiều

    def SoThanhPhan(self):
        da_tham = [False] * self.so_dinh
        
        def DFS(v):
            stack = [v]
            while stack:
                node = stack.pop()
                for neighbor in self.dinh_ke[node]:
                    if not da_tham[neighbor]:
                        da_tham[neighbor] = True
                        stack.append(neighbor)
        
        so_thanh_phan = 0
        for i in range(self.so_dinh):
            if not da_tham[i]:
                DFS(i)
                so_thanh_phan += 1
                
        return so_thanh_phan

    def ChuTrinh(self):
        da_tham = [False] * self.so_dinh
        parent = [-1] * self.so_dinh

        def DFS(v):
            da_tham[v] = True
            for neighbor in self.dinh_ke[v]:
                if not da_tham[neighbor]:
                    parent[neighbor] = v
                    if DFS(neighbor):
                        return True
                elif parent[v] != neighbor:
                    return True
            return False

        for i in range(self.so_dinh):
            if not da_tham[i]:
                if DFS(i):
                    return True
        return False

    def ChuaDinh(self, v):
        return 0 <= v < self.so_dinh

    def BacDinh(self, v):
        if self.ChuaDinh(v):
            return len(self.dinh_ke[v])
        else:
            raise ValueError(f"Đỉnh {v} không tồn tại trong đồ thị")

# Ví dụ sử dụng
dt = DoThi(5)
dt.them_canh(0, 1)
dt.them_canh(0, 2)
dt.them_canh(3, 4)

print(dt.BacDinh(0))  # Output: 2 (vì đỉnh 0 có hai cạnh nối với đỉnh 1 và 2)
print(dt.BacDinh(3))  # Output: 1 (vì đỉnh 3 có một cạnh nối với đỉnh 4)
print(dt.BacDinh(5))  # Raises ValueError (vì đỉnh 5 không tồn tại trong đồ thị)
