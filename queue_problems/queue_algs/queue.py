from nodes import Node


class Queue(object):
    """A first-in-last-out Queue."""
    def __init__(self, val=None):
        if val:
            node = Node(val)
            self.size = 1
        else:
            node = None
            self.size = 0
        self.top = node
        self.bottom = self.top

    @classmethod
    def fromarray(cls, array):
        """Initializer with array. Index 0 will be at the front of the queue"""
        if array:
            queue = cls()
            for x in array:
                queue.enqueue(x)
            return queue

    def enqueue(self, val):
        """Enqueues the value val onto the end of the queue"""
        bottom = Node(val)
        if self.isempty():
            self.top = bottom
        else:
            self.bottom.next = bottom

        self.bottom = bottom
        self.size += 1

    def dequeue(self):
        """Dequeues the value from the front of the queue"""
        if self.isempty():
            raise IndexError("Queue is empty")
        val = self.top.val
        self.top = self.top.next
        self.size -= 1
        return val

    def isempty(self):
        """Returns True if there is nothing in the Queue"""
        return not self.size

    def tostring(self):
        """Prints out the queue as a string"""
        print "<",
        curr = self.top
        while curr:
            print curr.val
            curr = curr.next
            if curr:
                print ",",
        print ">"

    def toarray(self):
        """Returns an array which contains the same elements as the Queue"""
        arr = []
        curr = self.top
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr

    def gettop(self):
        """Returns the value at the top of the Queue"""
        return self.top.val
