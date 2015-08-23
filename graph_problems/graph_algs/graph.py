from collections import defaultdict, deque


class Graph(object):
    """An implementation of an directed graph object using dictonary."""

    def __init__(self):
        """Creates an empty graph."""
        self._dict = defaultdict(set)

    def getdict(self):
        """Returns the dictionary that contains the structure of the graph."""
        return self._dict

    def getedges(self):
        """Returns the set of edges."""
        return set(
            [(vert, neighbor) for vert in self._dict.keys()
                for neighbor in self._dict[vert]]
        )

    def addnode(self, val):
        """If the node doesn't already exist, it creates a new one with no paths.
        If the node  already exists, this does nothing."""
        if val not in self._dict:
            self._dict[val]

    def addpath(self, a, b):
        """Adds a path from a to b if it doesn't already exist.
        If a or b doesn't exist, they will be added to the graph."""
        self._dict[a].add(b)

    def removepath(self, a, b):
        """If the path from a to b exists, it is removed.
        Otherwise, nothing happens."""
        if a in self._dict and b in self._dict[a]:
            self._dict[a].remove(b)

    def findallextendedcontacts(self):
        """Returns a dictionary of keys and their extended contacts."""
        return {
            key: self.depthfirstsearch(key) for key in self._dict.keys()}

    def depthfirstsearch(self, a, visited=None):
        """A depth first search from a."""
        if not visited:
            visited = set()
        visited.add(a)
        for vert in self._dict[a] - visited:
            self.depthfirstsearch(vert, visited)

        return visited

    def depthfirstsearch_path(self, a, b):
        """Uses DFS to find a path from a to b."""
        stack = [[a]]
        visited = set()
        while stack:
            path = stack.pop()
            vertex = path[-1]
            for nextvert in self._dict[vertex] - visited:
                visited.add(nextvert)
                if nextvert == b:
                    return path + [nextvert]
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
                queue.extend(self._dict[vertex] - visited)
        return visited

    def breadthfirstsearch_path(self, a, b):
        """Uses BFS to find shorted path from a to b."""
        queue = deque()
        queue.append([a])
        visited = set()
        while queue:
            path = queue.popleft()
            vertex = path[-1]
            for nextvert in self._dict[vertex] - visited:
                visited.add(nextvert)
                if nextvert == b:
                    return path + [nextvert]
                else:
                    queue.append(path + [nextvert])
