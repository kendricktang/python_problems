from collections import defaultdict, deque


class Graph(object):
    """An implementation of an directed graph object using dictonary."""

    def __init__(self):
        """Creates an empty graph."""
        self.__dict = defaultdict(set)

    def getdict(self):
        return self.__dict

    def addnode(self, val):
        """If the node doesn't already exist, it creates a new one with no paths.
        If the node  already exists, this does nothing."""
        if val not in self.__dict:
            self.__dict[val]

    def addpath(self, a, b):
        """Adds a path from a to b if it doesn't already exist.
        If a or b doesn't exist, they will be added to the graph."""
        self.__dict[a].add(b)

    def removepath(self, a, b):
        """If the path from a to b exists, it is removed.
        Otherwise, nothing happens."""
        if a in self.__dict and b in self.__dict[a]:
            self.__dict[a].remove(b)

    def depthfirstsearch(self, a, visited=None):
        """A depth first search from a."""
        if visited is None:
            visited = set()
        visited.add(a)
        for vert in self.__dict[a] - visited:
            self.depthfirstsearch(vert, visited)
        return visited

    def depthfirstsearch_paths(self, a, b):
        """Uses DFS to find all paths from a to b."""
        stack = [[a]]
        while stack:
            path = stack.pop()
            vertex = path[-1]
            for nextvert in self.__dict[vertex] - set(path):
                if nextvert is b:
                    yield path + [nextvert]
                else:
                    stack.append(path + [nextvert])

    def breadthfirstsearch(self, a):
        """Breadth first search from a."""
        visited = set()
        queue = deque()
        queue.append(a)
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(self.__dict[vertex] - visited)
        return visited

    def breadthfirstsearch_paths(self, a, b):
        """Uses BFS to find all paths from a to b."""
        queue = deque()
        queue.append([a])
        while queue:
            path = queue.popleft()
            vertex = path[-1]
            for nextvert in self.__dict[vertex] - set(path):
                if nextvert is b:
                    yield path + [nextvert]
                else:
                    queue.append(path + [nextvert])

    def shortestpath(self, a, b):
        try:
            return next(self.breadthfirstsearch_paths(a, b))
        except:
            return None


class UndirectedGraph(Graph):
    """An undirected graph. Subclass of Graph."""

    def addpath(self, a, b):
        super(UndirectedGraph, self).addpath(a, b)
        super(UndirectedGraph, self).addpath(b, a)

    def removepath(self, a, b):
        super(UndirectedGraph, self).removepath(a, b)
        super(UndirectedGraph, self).removepath(b, a)

if __name__ == "__main__":
    g = UndirectedGraph()
    g.addpath('A', 'B')
    g.addpath('A', 'C')
    g.addpath('B', 'A')
    g.addpath('B', 'D')
    g.addpath('B', 'E')
    g.addpath('C', 'A')
    g.addpath('C', 'F')
    g.addpath('D', 'B')
    g.addpath('E', 'B')
    g.addpath('E', 'F')
    g.addpath('F', 'C')
    g.addpath('F', 'E')
    print g.depthfirstsearch('A')
    print g.depthfirstsearch('C')
    print list(g.depthfirstsearch_paths('A', 'F'))
    print g.breadthfirstsearch('A')
    print list(g.breadthfirstsearch_paths('A', 'F'))
    print g.shortestpath('A', 'F')
