class Stack:
    def __init__(self) -> None:
        self.list = []

    def __str__(self) -> str:
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"

    def pop(self):
        if self.list == []:
            return "There is not any element in the stack"
        else:
            return self.list.pop()


class Queue:
    def __init__(self) -> None:
        self.first = Stack()
        self.last = Stack()

    def enqueue(self, value):
        self.first.push(value)

    def dequeue(self):
        loop = len(self.first.list)
        for _ in range(loop):
            temp = self.first.pop()
            self.last.push(temp)
        result = self.last.pop()
        loop = len(self.last.list)
        for _ in range(loop):
            temp = self.last.pop()
            self.first.push(temp)
        return result

    def __str__(self) -> str:
        values = [str(x) for x in self.first.list]
        return '\n'.join(values)


customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.dequeue()
print(customQueue.__str__())