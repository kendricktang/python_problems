from nodes import Node

class Stack(object):
    """Regular Stack object. First-in-last-out."""
    
    def __init__(self, val = None):
        """Initializer with single value."""
        if val:
            self.top = Node(val)
            self.size = 1
        else:
            self.top = val
            self.size = 0
    
    @classmethod
    def fromarray(cls, array):
        """Initializer with array. Highest index will be at the top."""
        if array:
            stack = cls(array[0])
            for i in xrange(1, len(array)):
                stack.push(array[i])
            return stack
        
    def pop(self):
        """Pops off the top value of the stack."""
        if self.top:
            val = self.top.val
            self.top = self.top.next
            self.size -= 1
            return val            
        
    def push(self, val):
        """Pushes on a new value to the top of the stack."""
        self.top = Node(val, next = self.top)
        self.size += 1
    
    def isempty(self):
        """Typical isempty method: checks if the stack is empty."""
        return not self.size
        
    def tostring(self):
        print "<",
        curr = self.top
        while curr:
            print curr.val,
            curr = curr.next
            if curr:
                print ",",
        print ">"
        
    def toarray(self):
        arr = []
        curr = self.top
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr

