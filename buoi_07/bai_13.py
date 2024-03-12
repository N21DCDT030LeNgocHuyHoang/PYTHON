def __init__(self):
    temp_node = self.head
    result = ''
    while temp_node is not None:
        result += str (node.value)
        if temp_node.next is not None:
            result += '->'
            temp_node = temp_node.next
            return result
new_Linked_List = LinkedList()
new_Linked_List.append(10)
new_Linked_List.append(20)
print(new_Linked_List)        