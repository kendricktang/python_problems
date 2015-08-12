import unittest
from graph_algs.maze import MazeSolver as MS
from graph_algs.maze import Coordinate as Coord


class TestMazeSolver(unittest.TestCase):
    """A test suite for MazeSolver class. Specifically the maze solving part."""

    def test_trivial_fail(self):
        """Most trivial fail case."""
        maze = [
            [0]
        ]
        ms = MS(maze=maze)
        start = Coord(0, 0)
        end = Coord(0, 0)
        path = ms.solvemaze(start, end)
        self.assertEqual(path, -1)

    def test_trivial_pass(self):
        """Most trivial pass case."""
        maze = [
            [1]
        ]
        ms = MS(maze=maze)
        start = Coord(0, 0)
        end = Coord(0, 0)
        path = ms.solvemaze(start, end)
        self.assertTrue(
            confirmmazeseq(ms.maze, path, start, end))

    def test_textbookcase_pass(self):
        """Example from textbook. Start and end picked for success."""
        maze = [
            [0, 1, 1, 1, 1, 1, 0, 0, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 0, 1, 1, 0, 0, 1, 0, 0],
            [1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [0, 1, 0, 0, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
        ]
        ms = MS(maze=maze)
        start = Coord(9, 0)
        end = Coord(0, 9)
        path = ms.solvemaze(start, end)
        self.assertTrue(
            confirmmazeseq(ms.maze, path, start, end))

    def test_textbookcase_fail(self):
        """Example from textbook. Start and end picked for failure."""
        maze = [
            [0, 1, 1, 1, 1, 1, 0, 0, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 0, 1, 1, 0, 0, 1, 0, 0],
            [1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [0, 1, 0, 0, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
        ]
        ms = MS(maze=maze)
        start = Coord(0, 0)
        end = Coord(0, 1)
        path = ms.solvemaze(start, end)
        self.assertEqual(path, -1)


def isvalidstep(maze, s, t):
    """Checks to see if s and t are not walls.
    Also checks to see if s and t are one step away from each other."""
    if not maze[s.x][s.y] or not maze[t.x][t.y]:
        return False
    return s.manhattandistance(t) == 1


def confirmmazeseq(maze, path, start, end):
    """Walks through the path and checks to see if each step is valid."""
    if start != path[0] or end != path[-1]:
        return False
    prev = start
    for coord in path[1:]:
        if not isvalidstep(maze, prev, coord):
            return False
        prev = coord
    return True


if __name__ == "__main__":
    unittest.main()
