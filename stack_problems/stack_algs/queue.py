from max_stack import MaxStack


class Queue(object):
    """A first in first out Queue implemented with two stacks.
    This also implements a max function.
    """

    def __init__(self):
        self.s1 = MaxStack()
        self.s2 = MaxStack()

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

    def getmax(self):
        if self.s1.isempty():
            if self.s2.isempty():
                raise TypeError("Queue is empty")
            else:
                return self.s2.getmax()
        if self.s2.isempty():
            return self.s1.getmax()
        return max(self.s1.getmax(), self.s2.getmax())
