class Stack:
    def __init__ (self,maxSize):
        self.maxSize = maxSize
        self.list=[]
        
    def __str__ (self):
        values = self.list.reverse()
        values = [str(x)for x in self.list]
        return'\n'.join(values)
#isEmpty
def isEmpty(self):
    if self.list ==[]:
        return True
    else:
        return False
# isFull
def isFull(self):
    if len(self.list)==self.maxSize:
        return True
    else:
        return False
#push
def push (self,value):
    if self.isFull():
        if self.isFull():
            return"The stack is full"
        else:
            self.list.append(value)
            return"The element has been successfully inserted"
customStack=Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
        