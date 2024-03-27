class HanoiTower:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.towers = [[], [], []]

        # Khởi tạo tháp ban đầu với tất cả đĩa nằm ở tầng đầu tiên
        for i in range(num_disks, 0, -1):
            self.towers[0].append(i)

    def move_disks(self, n, source, target, auxiliary):
        if n >= 1:
            # Di chuyển n-1 đĩa từ nguồn đến tháp trung gian
            self.move_disks(n-1, source, auxiliary, target)

            # Di chuyển đĩa còn lại từ nguồn đến đích
            disk = self.towers[source].pop()
            self.towers[target].append(disk)
            print(f"Di chuyển đĩa {disk} từ tháp {source + 1} đến tháp {target + 1}")

            # Di chuyển n-1 đĩa từ tháp trung gian đến đích
            self.move_disks(n-1, auxiliary, target, source)

    def solve(self):
        print("Bước di chuyển các đĩa:")
        self.move_disks(self.num_disks, 0, 2, 1)

    def print_towers(self):
        for i, tower in enumerate(self.towers):
            print(f"Tháp {i + 1}: {tower}")


# Sử dụng
num_disks = 3  # Số lượng đĩa
hanoi = HanoiTower(num_disks)
print("Trạng thái ban đầu của các tháp:")
hanoi.print_towers()
hanoi.solve()
print("\nTrạng thái cuối cùng của các tháp:")
hanoi.print_towers()
