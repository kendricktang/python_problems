class Node(object):
    """A single-linked node for a linked list."""
    def __init__(self, val, next=None):
        """A simple initializer for the Node class."""
        self.val = val
        self.next = next


class BinaryNode(object):
    """A single-linked node for a linked list."""
    def __init__(self, val, left=None, right=None):
        """A simple initializer for the Node class."""
        self.val = val
        self.left = left
        self.right = right
    
    def haschildren(self):
        """Checks for the presence of any child"""
        return self.left or self.right
    
    def hasnext(self, val):
        """Checks for a left or right child, depending on the value"""
        return ((val >= self.val and self.right) 
            or (val < self.val and self.left))

    def getnext(self, val):
        """Gets the left or right child, depending on the value"""
        if val >= self.val:
            return self.right
        return self.left
    
    def setnext(self, val):
        """If it is legal to create a child, then a child is created.
        Otherwise, an error is raised.
        """
        
        if val >= self.val and not self.right:
            self.right = BinaryNode(val)
        elif val < self.val and not self.left:
            self.left = BinaryNode(val)
        else:
            raise Error("Cannot set next, there is a node in the way")