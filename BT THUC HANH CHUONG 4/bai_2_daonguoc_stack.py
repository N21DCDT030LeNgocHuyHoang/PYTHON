class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def DaoNguoc(self):
        if self.head is None:
            return

        stack = []
        current = self.head
        while current:
            stack.append(current)
            current = current.next

        self.head = stack.pop()
        current = self.head
        while stack:
            current.next = stack.pop()
            current = current.next
        current.next = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

# Sử dụng
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)

print("Danh sách ban đầu:")
llist.display()

print("\nDanh sách sau khi đảo ngược:")
llist.DaoNguoc()
llist.display()
