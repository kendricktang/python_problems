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
