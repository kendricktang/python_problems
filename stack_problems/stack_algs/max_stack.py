from stack import Stack


class MaxStack(Stack):
    def __init__(self, val=None):
        """Initializes a stack which has a getmax O(1) get max method."""
        if val:
            super(MaxStack, self).__init__(val=(val, val))
        else:
            super(MaxStack, self).__init__()

    def push(self, val):
        """Pushes a new value on top of the stack."""
        if self.isempty():
            super(MaxStack, self).push((val, val))
        else:
            super(MaxStack, self).push((val, max(self.top.val[1], val)))

    def pop(self):
        val = super(MaxStack, self).pop()
        return val[0]

    def getmax(self):
        """Returns the maximum value in the stack."""
        if self.isempty():
            return IndexError("Stack is empty")
        if self.top:
            return self.top.val[1]


class MaxStackAlt(Stack):
    def __init__(self, val):
        """Initializes a stack which has a getmax O(1) get max method."""
        self.maxstack = Stack([val, 1])
        super(MaxStackAlt, self).__init__(val)

    def push(self, val):
        """Pushes a new value on top of the stack."""
        if self.maxstack.top:
            if val == self.maxstack.top.val[0]:
                self.maxstack.top.val[1] += 1
            elif val > self.maxstack.top.val[0]:
                self.maxstack.push([val, 1])
        else:
            self.maxstack.push([val, 1])

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
