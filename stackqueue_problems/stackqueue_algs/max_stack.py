class Stack(object):
    """Regular Stack object. First-in-last-out."""
    
    def __init__(self, val):
        """Initializer with single value."""
        self.top = LinkedList(val)
    
    @classmethod
    def fromarray(cls, array):
        """Initializer with array. Highest index will be at the top."""
        if array:
            maxstack = cls(array[0])
            for i in xrange(1, len(array)):
                maxstack.push(array[i])
            return maxstack
        
    def pop(self):
        """Pops off the top value of the stack."""
        if self.top:
            val = self.top.val
            self.top = self.top.next
            return val            
        
    def push(self, val):
        """Pushes on a new value to the top of the stack."""
        self.top = LinkedList(val, next = self.top)
    
    def isempty(self):
        """Typical isempty method: checks if the stack is empty."""
        return self.top.next


class MaxStack(Stack):
    def __init__(self, val):
        """Initializes a stack which has a getmax O(1) get max method."""
        super(MaxStack, self).__init__((val,val))
    
    def push(self, val):
        """Pushes a new value on top of the stack."""
        super(MaxStack, self).push((val, max(self.top.val[1], val)))
    
    def pop(self):
        val = super(MaxStack, self).pop()
        return val[0]
    
    def getmax(self):
        """Returns the maximum value in the stack."""
        if self.top:
            return self.top.val[1]


class MaxStackAlt(Stack):
    def __init__(self, val):
        """Initializes a stack which has a getmax O(1) get max method."""
        self.maxstack = Stack([val,1])
        super(MaxStackAlt, self).__init__(val)

    def push(self, val):
        """Pushes a new value on top of the stack."""
        if self.maxstack.top:
            if val == self.maxstack.top.val[0]:
                self.maxstack.top.val[1] += 1
            elif val > self.maxstack.top.val[0]:
                self.maxstack.push([val,1])
        else:
            self.maxstack.push([val,1])
        
        super(MaxStackAlt, self).push(val)

    def pop(self):
        """Pops off the top value of the stack."""
        if self.top:
            if self.top.val == self.getmax():
                if self.maxstack.top.val[1] > 1:
                    self.maxstack.top.val[1] -= 1
                else:
                    self.maxstack.pop()
            
            return super(MaxStackAlt, self).pop()
    
    def getmax(self):
        """Returns the maximum value in the stack."""
        return self.maxstack.top.val[0]

class LinkedList(object):
    """A singley-linked list."""
    def __init__(self, val, next=None):
        """A simple initializer for the LinkedList class."""
        self.val = val
        self.next = next
