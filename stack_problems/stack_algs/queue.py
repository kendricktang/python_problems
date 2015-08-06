from stack import Stack


class Queue(object):
    """A first in first out Queue implemented with two stacks."""

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, val):
        self.s1.push(val)

    def dequeue(self):
        if self.s2.isempty():
            while not self.s1.isempty():
                self.s2.push(self.s1.pop())
        if self.s2.isempty():
            raise IndexError("Queue is empty")
        return self.s2.pop()

    def isempty(self):
        return self.s1.isempty() and self.s2.isempty()
