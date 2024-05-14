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

# Ví dụ sử dụng
dt = DoThi(5)
dt.them_canh(0, 1)
dt.them_canh(0, 2)
dt.them_canh(3, 4)

print(dt.SoThanhPhan())  # Output: 2
