class Node:
    def __int__(self,value):
        self.value = value
        self.next = None
def append (self,value):
    new_node= Node(value)
    if self.head is None:
        self.head=new_node
    else:
        self.tail.next=new_node
        self.tail=new_node
    self.length=1
    
        