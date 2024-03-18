class Stack:
    def __init__(self, maxSize) -> None:
        self.maxSize = maxSize
        self.list = []

    def __str__(self) -> str:
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def push(self, value):
        if len(self.list) == self.maxSize:
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element has been successfully inserted"

    def devideStack(self):
        length = len(self.list)
        list1 = list(self.list[0:int(length/3)])
        list2 = list(self.list[int(length/3):int(2*length/3)])
        list3 = list(self.list[int(2*length/3):length])
        return list1, list2, list3


customStack = Stack(9)
customStack.push(0)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.push(5)
customStack.push(6)
customStack.push(7)
customStack.push(8)
print(customStack.devideStack())