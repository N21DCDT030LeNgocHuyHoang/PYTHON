
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

    def pop(self):
        if self.list == []:
            return "There is not any element in the stack"
        else:
            return self.list.pop()

    def min(self):
        if self.list == []:
            return "There is not any element in the stack"
        else:
            return min(self.list)


customStack = Stack(6)
customStack.push(5)
print(customStack.min())
customStack.push(6)
print(customStack.min())
customStack.push(3)
print(customStack.min())
customStack.push(7)
print(customStack.min())
customStack.pop()
print(customStack.min())
customStack.pop()
print(customStack.min())