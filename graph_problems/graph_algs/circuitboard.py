def isdivisible(pins, wirecons):
    """Pins is a set of pins. Wirecons must be a set of 2-tuples of pins.
    Returns whether the pins can be divided onto two separate boards."""
    mypins = {}
    for pin in pins:
        mypins[pin] = 0
    wirecons = wirecons.copy()

    # O(V * E)
    for pin in mypins:
        if not mypins[pin]:
            # If pin hasn't been visited, arbitrarily mark it as on pcb 1.
            mypins[pin] = 1

        # Generate neighbors
        neighbors = set()
        for wirecon in wirecons:
            if pin in wirecon:
                neighbors.add(wirecon[pin == wirecon[0]])

        for otherpin in neighbors:
            if not mypins[otherpin]:
                # if otherpin hasn't been visited, mark it as the opposite
                # of pin.
                mypins[otherpin] = -mypins[pin]
            elif mypins[otherpin] + mypins[pin]:
                # the pins are on the same PCB when they shouldn't be.
                return False
    return True


"""0, 9, 14"""
if __name__ == "__main__":
    pins = set(xrange(22))
    wirecons = set(
        [
            (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8),
            (0, 9), (1, 10), (2, 11), (3, 12), (12, 5), (5, 13), (13, 7),
            (9, 10), (10, 11), (11, 12),
            (9, 14), (10, 15), (11, 16), (12, 17), (13, 19), (13, 21),
            (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 20), (20, 21)
        ]
    )
    print isdivisible(pins, wirecons)  # True.
