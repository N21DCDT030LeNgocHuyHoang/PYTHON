class _Node:
    __slots__ = '_element','_next'
    
    def __init__ (self, element, next):
        self.element = element
        self._next = next
        
class QueuesLinked:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0
    
    def __len__ (self):
        return self._size
    def isempty(self):
        return self._size == 0
    