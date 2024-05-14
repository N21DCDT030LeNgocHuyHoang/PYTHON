class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class CayNhiPhan():
    def __init__(self):
        self.root = None

    def SoNutLa(self):
        return self._SoNutLa(self.root)

    def _SoNutLa(self, node):
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return 1
        else:
            return self._SoNutLa(node.left) + self._SoNutLa(node.right)
        
tree = CayNhiPhan()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.right = Node(6)
tree.root.right.right.right = Node(7)

print("Số nút lá của cây là:", tree.SoNutLa())
        