class Node: 
  
    def __init__(self, value): 
        self.value = value
        self.next = None
  
class LinkedList: 
  
    def __init__(self): 
        self.head = None
   
    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 
        
    def push(self, value): 
        new_node = Node(value) 
        new_node.next = self.head 
        self.head = new_node 
  
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (temp.value,end=" ") 
            temp = temp.next
   
llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(85) 
  
print ("Given Linked List") 
llist.printList() 
llist.reverse() 
print ("\nReversed Linked List") 
llist.printList()