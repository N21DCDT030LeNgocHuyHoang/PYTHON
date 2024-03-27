class LinkedList:
    # Code khác như trên đã định nghĩa

    def InNguoc_recursive(self, node):
        if node is None:
            return
        self.InNguoc_recursive(node.next)
        print(node.data, end=" ")

    def InNguoc_recursive_start(self):
        self.InNguoc_recursive(self.head)

# Sử dụng
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)

print("Danh sách ban đầu:")
current = llist.head
while current:
    print(current.data, end=" ")
    current = current.next

print("\nDanh sách sau khi in ngược (đệ qui):")
llist.InNguoc_recursive_start()
