def prepend(self,value):
    new_node = Node(value)
    if self.head is None:
        self.head = new_node
        self.tail = new_node
    else:
        new_node.next = self.head
        self.head = new_node
    self.length += 1
    new_Linked_List = LinkedList()
    new_Linked_List.append(10)
    new_Linked_List.append(20)
    new_Linked_List.append(30)
    print(new_Linked_List)
    new_Linked_List.append(40)
    print(new_Linked_List)