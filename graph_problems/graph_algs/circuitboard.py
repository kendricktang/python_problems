def isdivisible(pins, wirecons):
    """Pins is a set of pins. Wirecons must be a set of 2-tuples of pins.
    Returns whether the pins can be divided onto two separate boards."""
    mypins = {}
    BOARD = 1

    # Assign pins to neither board.
    for pin in pins:
        mypins[pin] = 0

    # O(V * E)
    for pin in mypins:
        if not mypins[pin]:
            # If pin hasn't been visited, arbitrarily mark it as on BOARD.
            mypins[pin] = BOARD

        # Generate neighbors
        neighbors = set()
        for wirecon in wirecons:
            if pin in wirecon:
                neighbors.add(getotherpin(wirecon, pin))

        for otherpin in neighbors:
            if not mypins[otherpin]:
                # if otherpin hasn't been visited, mark it as the opposite
                # of pin.
                markasopposite(mypins, pin, otherpin)
            elif onsameboard(mypins, pin, otherpin):
                # the pins are on the same PCB when they shouldn't be.
                return False
    return True


def markasopposite(pinset, pin, otherpin):
    """If pin belongs to BOARD, place otherpin on the other board..
    If pin belongs to the other board, place otherpin on BOARD."""
    pinset[otherpin] = -pinset[pin]


def onsameboard(mypins, pin0, pin1):
    """Returns True if pin0 and pin1 are both on the same board."""
    return bool(mypins[pin0] + mypins[pin1])


def getotherpin(pinpair, pin):
    """Given a 2-tuple of pins, and a pin in the 2-tuple,
    the other pin is returned."""
    return pinpair[pin == pinpair[0]]
