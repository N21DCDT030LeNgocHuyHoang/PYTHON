import random


class DEQueArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def addfirst(self, e):
        self._data.insert(0, e)

    def addlast(self, e):
        self._data.append(e)

    def removefirst(self):
        if self.isempty():
            print('DEQue is empty')
            return
        return self._data.pop(0)

    def removelast(self):
        if self.isempty():
            print('DEQue is empty')
            return
        return self._data.pop()


class Queue:
    def __init__(self) -> None:
        self.dogs = DEQueArray()
        self.cats = DEQueArray()

    def EnqueueDog(self, value):
        self.dogs.addlast(value)

    def EnqueueCat(self, value):
        self.cats.addlast(value)

    def EnqueueAny(self, value):
        randNum = random.randint(1, 2)
        if randNum == 1:
            self.EnqueueCat(value)
        else:
            self.EnqueueDog(value)

    def DequeueDog(self):
        return self.dogs.removefirst()

    def DequeueCat(self):
        return self.cats.removefirst()

    def DequeueAny(self):
        randNum = random.randint(1, 2)
        if randNum == 1:
            self.DequeueCat()
        else:
            self.DequeueDog()

    def printDogs(self):
        values = ["dog " + str(x) for x in self.dogs._data]
        return '\t'.join(values)

    def printCats(self):
        values = ["cat " + str(x) for x in self.cats._data]
        return '\t'.join(values)


customQueue = Queue()
customQueue.EnqueueDog(1)
customQueue.EnqueueDog(2)
customQueue.EnqueueDog(3)
customQueue.EnqueueCat(1)
customQueue.EnqueueCat(2)
customQueue.DequeueDog()
customQueue.DequeueAny()
print(customQueue.printDogs())
print(customQueue.printCats())