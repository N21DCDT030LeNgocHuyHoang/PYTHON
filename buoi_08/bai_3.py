class Node:
    def __init__ (self,value=None):
        self.value = value
        self.next =next
class LinkedList:
    def __init__(self):
        self.head = None
class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
        if self.LinkedList.head == Node:
            return True
        else:
            return False
customStack = Stack()
print(customStack.isEmpty())

def push(self,value):
    node = Node(value)
    node.next = self.LinkedList.head = node
    self.LinkedList.head = node
customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)

def pop(self):
    if self.isEmpty():
        if self.isEmpty():
            return "There is not any element in the Stack"
        else:
            nodeValue = self.LinkedList.value
            self.LinkedList.head= self.LinkedList.head.next
            return nodeValue
customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print("-----------")
customStack.pop()
print(customStack)

        