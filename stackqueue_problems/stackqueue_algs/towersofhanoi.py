from stack import Stack

class TowerOfHanoi(Stack):
    """Essentially a Stack, with a name."""
    
    def __init__(self, name, val = None):
        """Initializes a TowerOfHanoi with a specified name,"""
        super(TowerOfHanoi, self).__init__(val)
        self.name = name
    
    @classmethod
    def fromarray(cls, array, name):
        """Initiate a TowerOfHanoi with an array"""
        if array:
            tower = cls(name, val = array[0])
            for i in xrange(1, len(array)):
                tower.push(array[i])
            return tower
    
    def tostring(self):
        """Prints out the name of the tower, 
        and the elements in order from top to bottom.
        """
        print self.name,
        super(TowerOfHanoi, self).tostring()
        

def towersofhanoi(size, suppress = False):
    """Creates three towers of hanoi.
    The first one is full of discs, and the other two are empty.
    The discs are legally moved to the second disc, 
    and the moves are printed out.
    """
    current = TowerOfHanoi.fromarray(xrange(size,0,-1), "First")
    target = TowerOfHanoi("Second")
    helper = TowerOfHanoi("Third")
    
    towersofhanoi_helper(current, target, helper, size, suppress)    
    
    return target

def towersofhanoi_helper(current, target, helper, n, suppress):
    """Recursive helper for towersofhanoi"""
    if n == 1:
        val = current.pop()
        target.push(val)
        if not suppress:
            print "From: " + current.name + ", Target: " + target.name + ", val: %d" % val
    else:
        towersofhanoi_helper(current, helper, target, n-1, suppress)
        val = current.pop()
        target.push(val)
        if not suppress:
            print "From: " + current.name + ", Target: " + target.name + ", val: %d" % val
        towersofhanoi_helper(helper, target, current, n-1, suppress)

if __name__ == "__main__":
    towersofhanoi(4)
