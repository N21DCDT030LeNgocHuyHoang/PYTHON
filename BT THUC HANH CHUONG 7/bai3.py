class DoThi:
    def __init__(self, so_dinh):
        self.so_dinh = so_dinh
        self.dinh_ke = [[] for _ in range(so_dinh)]

    def them_canh(self, u, v):
        self.dinh_ke[u].append(v)
        self.dinh_ke[v].append(u)  # Vì là đồ thị vô hướng, nên ta thêm cạnh ở cả hai chiều

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

# Ví dụ sử dụng
dt = DoThi(5)
dt.them_canh(0, 1)
dt.them_canh(0, 2)
dt.them_canh(1, 2)
dt.them_canh(3, 4)

print(dt.ChuTrinh())  # Output: True (vì có chu trình 0-1-2-0)
