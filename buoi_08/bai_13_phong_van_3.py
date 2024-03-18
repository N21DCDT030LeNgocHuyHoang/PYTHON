class SubStack:
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

    def pop(self):
        if self.list == []:
            return "There is not any element in the stack"
        else:
            return self.list.pop()

    def __str__(self) -> str:
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)


class Stack:
    def __init__(self, maxSize) -> None:
        self.stack = [SubStack(maxSize)]
        self.maxSize = maxSize

    def pushAt(self, index, value):
        if index >= len(self.stack):
            return "Không thể thêm vào"
        if len(self.stack[index].list) == self.stack[index].maxSize:
            self.stack.append(SubStack(self.maxSize))
            self.stack[index+1].push(value)
        else:
            self.stack[index].push(value)

    def popAt(self, index):
        if index >= len(self.stack):
            return "Không thể thêm vào"
        if len(self.stack[index].list) == 0:
            return "Stack rỗng"
        else:
            self.stack[index].pop()


customStack = Stack(2)
customStack.pushAt(0, 1)
customStack.pushAt(0, 2)
customStack.pushAt(0, 3)
customStack.popAt(0)
print(customStack.stack[0].__str__())
print(customStack.stack[1].__str__())