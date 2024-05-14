class DoThi:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def themCanh(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFS(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.DFS(i, visited)

    def LienThong(self):
        visited = [False] * self.V
        self.DFS(0, visited)
        for i in range(1, self.V):
            if not visited[i]:
                return False
        return True

# Ví dụ sử dụng
g = DoThi(5)
g.themCanh(0, 1)
g.themCanh(0, 2)
g.themCanh(1, 2)
g.themCanh(3, 4)
print("Đồ thị là liên thông:", g.LienThong())
