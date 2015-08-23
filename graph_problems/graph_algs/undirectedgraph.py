from graph import Graph


class UndirectedGraph(Graph):
    """An undirected graph. Subclass of Graph."""

    def addpath(self, a, b):
        """Add a path to an undirected graph."""
        super(UndirectedGraph, self).addpath(a, b)
        super(UndirectedGraph, self).addpath(b, a)

    def removepath(self, a, b):
        """Remove a path from an undirected graph."""
        super(UndirectedGraph, self).removepath(a, b)
        super(UndirectedGraph, self).removepath(b, a)

    def checkconnectivity_2E(self):
        """A connected undirected graph is 2E-connected if there exists an edge
        that can be removed without forming a disconnect. This is equivalent to
        there being a cycle in the graph. Uses DFS.

        Returns True if the graph is connected and 2E-connected.
        Returns False if the graph is connected and not 2E-connected.
        If the graph is not connected, the returned value describes the
        connectivity of the connected subgraph containing self._dict.keys()[0].
        """
        if len(self._dict) < 2:
            return True

        node = self._dict.keys()[0]
        stack = [[node]]

        while stack:
            path = stack.pop()
            node = path[-1]
            for neighbor in self._dict[node]:
                if neighbor not in path:
                    stack.append(path + [neighbor])
                elif neighbor in path[:-2]:
                    # Found a cycle!
                    return True
        return False

    def checkconnectivity_2A(self):
        """A connected undirected graph is 2A-connected if for every edge,
        if it is removed the graph remains connected. This is equivalent to
        checking whether each edge is part of a cycle. Uses DFS.

        Returns True if the graph is connected and 2A-connected.
        Returns False if the graph is connected and not 2A-connected.
        If the graph is not connected, the returned value describes the
        connectivity of the connected subgraph containing self._dict.keys()[0].
        """
        if len(self._dict) < 2:
            return True

        node = self._dict.keys()[0]
        stack = [[node]]
        edgeset = self.getedges()

        while stack and edgeset:
            path = stack.pop()
            node = path[-1]
            for neighbor in self._dict[node]:
                if neighbor not in path:
                    stack.append(path + [neighbor])
                elif neighbor in path[:-2]:
                    # Found a cycle!
                    self._removeedges(path, edgeset)

        if edgeset:
            # If edges remain, then there are edges that weren't part of cycles.
            return False
        return True

    def _removeedges(self, path, edgeset):
        """Walks through a path and removes edges from the edge set."""
        for edge in self._getedgesfrompath(path):
            _edge = (edge[1], edge[0])
            if edge in edgeset:
                edgeset.remove(edge)
            if _edge in edgeset:
                edgeset.remove(_edge)

    def _getedgesfrompath(self, path):
        """Generates all edges from a path"""
        for ind in xrange(len(path)-1):
            yield (path[ind], path[ind+1])

    def checkconstraints(self, equalities, inequalities):
        """Determines whether the equalities and inequalities can be satisfied
        concurrently. I'm not implementing this function."""
        # Create graph using equalities
        # Using DFS-like algorith, determine the connected parts of the graph
        # For each inequality, make sure the two elements are disconnected.
        pass
