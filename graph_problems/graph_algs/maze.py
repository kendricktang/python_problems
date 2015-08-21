class MazeSolver(object):
    """A class for solving mazes. Mazes must be rectangular 2-D arrays
    where a 0 means that region is a wall, and a 1 one means that region is
    a path."""

    def __init__(self, maze=[]):
        """Creates a new mazesolver object.
        It can be initialized with no maze."""
        if maze:
            self.changemaze(maze)

    def changemaze(self, maze):
        """Changes the maze to be solved. Maze must be 2-D."""
        if not maze[0]:
            raise TypeError("Maze must have exactly 2 dimensions.")
        self.maze = maze
        self.width = len(maze)
        self.height = len(maze[0])

    def solvemaze(self, start, end):
        """Finds a path (if it exists), using DFS.
        Start and end must be coordinates."""
        if not self.maze[start.x][start.y]:
            return -1
        if start == end:
            return [start]

        stack = [[start]]
        visited = set()
        while stack:
            path = stack.pop()
            vertex = path[-1]
            for nextvert in self.findneighbors(vertex) - visited:
                visited.add(nextvert)
                if nextvert == end:
                    return path + [nextvert]
                else:
                    stack.append(path + [nextvert])
        return -1

    def findneighbors(self, vertex):
        neighbors = set()
        shift = ((0, -1), (0, 1), (-1, 0), (1, 0))
        for x, y in shift:
            newcoord = Coordinate(vertex.x + x, vertex.y + y)
            if (self.validcoordinate(newcoord) and
                    self.maze[newcoord.x][newcoord.y]):
                neighbors.add(newcoord)
        return neighbors

    def validcoordinate(self, coord):
        """Checks to see if the coordinates are within the maze."""
        return (
            coord.x >= 0 and coord.x < self.width and
            coord.y >= 0 and coord.y < self.height)


class Coordinate(object):
    """An object which represents a space in a maze."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def manhattandistance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __eq__(self, other):
        return (
            self.x is other.x and
            self.y is other.y)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.__repr__())
