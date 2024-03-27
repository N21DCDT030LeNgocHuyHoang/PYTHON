class Solution:
    def __init__(self):
        self.max_area = 0

    def find_max_area(self, matrix):
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        visited = [[False] * cols for _ in range(rows)]

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] == 0 or visited[i][j]:
                return 0

            visited[i][j] = True
            area = 1  # Đếm ô hiện tại

            # Duyệt các ô kề cạnh
            area += dfs(i + 1, j)  # Ô dưới
            area += dfs(i - 1, j)  # Ô trên
            area += dfs(i, j + 1)  # Ô bên phải
            area += dfs(i, j - 1)  # Ô bên trái

            return area

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1 and not visited[i][j]:
                    self.max_area = max(self.max_area, dfs(i, j))

        return self.max_area


# Hàm main để kiểm tra
def main():
    matrix = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]
    ]

    solution = Solution()
    max_area = solution.find_max_area(matrix)
    print("Max area of rectangular islands:", max_area)


if __name__ == "__main__":
    main()
