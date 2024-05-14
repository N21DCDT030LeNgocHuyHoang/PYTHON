class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class CayNhiPhan():
    def __init__(self):
        self.root = None
    
    def SoNut(self):
        return self._SoNut(self.root)

    def _SoNut(self, node):
        if node is None:
            return 0
        else:
            return self._SoNut(node.left) +self._SoNut(node.right) + 1
        
tree = CayNhiPhan()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.right.right = Node(5)

print("Số nút của cây là:", tree.SoNut())