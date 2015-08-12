import unittest
from graph_algs.circuitboard import isdivisible


class TestFindExtendedContacts(unittest.TestCase):
    """A test suite for circuitboard.isdivisible()."""

    def test_noconnections(self):
        """Test case for when there are no wire connections. Trivial True."""
        pins = set(xrange(42))
        wirecons = set(
            [
            ]
        )
        self.assertTrue(isdivisible(pins, wirecons))

    def test_nopins(self):
        """Test case for when there are no pins. Trivial True."""
        pins = set()
        wirecons = set(
            [
                (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8),
                (0, 9), (1, 10), (2, 11), (3, 12), (12, 5), (5, 13), (13, 7),
                (9, 10), (10, 11), (11, 12)
            ]
        )
        self.assertTrue(isdivisible(pins, wirecons))

    def test_base_nontrivial_pass_case(self):
        """Simple (maybe simplest) non-trivial pass case:
        two pins and one wire."""
        pins = set([0, 1])
        wirecons = set([(0, 1)])
        self.assertTrue(isdivisible(pins, wirecons))

    def test_base_nontrivial_fail_case(self):
        """Simplest non-trivial fail case: three wires in a cycle."""
        pins = set([0, 1, 2])
        wirecons = set([(0, 1), (1, 2), (2, 0)])
        self.assertFalse(isdivisible(pins, wirecons))

    def test_testbookcase_pass(self):
        """Pin and connection set from textbook."""
        pins = set(xrange(22))
        wirecons = set(
            [
                (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8),
                (0, 9), (1, 10), (2, 11), (3, 12), (12, 5), (5, 13), (13, 7),
                (9, 10), (10, 11), (11, 12),
                (9, 14), (10, 15), (11, 16), (12, 17), (13, 19), (13, 21),
                (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 20),
                (20, 21)
            ]
        )
        self.assertTrue(isdivisible(pins, wirecons))

    def test_testbookcase_fail(self):
        """Modified for failure: pin and connection set from textbook."""

        pins = set(xrange(22))
        wirecons = set(
            [
                (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8),
                (0, 9), (1, 10), (2, 11), (3, 12), (12, 5), (5, 13), (13, 7),
                (9, 10), (10, 11), (11, 12),
                (9, 14), (10, 15), (11, 16), (12, 17), (13, 19), (13, 21),
                (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 20),
                (20, 21), (20, 0)
            ]
        )
        self.assertFalse(isdivisible(pins, wirecons))


if __name__ == "__main__":
    unittest.main()
