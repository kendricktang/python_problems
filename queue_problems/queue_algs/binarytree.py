from queue import Queue


def printbinarytree(rootnode):
    """Returns a string of a binary tree in level order and left to right."""
    returnstr = ""
    queue = Queue(rootnode)
    count = 1
    while not queue.isempty():
        curr = queue.dequeue()
        if curr.left:
            queue.enqueue(curr.left)
        if curr.right:
            queue.enqueue(curr.right)

        returnstr += str(curr.val)
        if not queue.isempty():
            returnstr += ","

        count += 1
    return returnstr
