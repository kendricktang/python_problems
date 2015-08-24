def findminmax(array):
    """Returns (min, max) in no more than roof(3n/2) - 2 comparisons."""
    if len(array) == 0:
        raise IndexError("Array has to have stuff in it.")
    if len(array) == 1:
        return (array[0], array[0])

    # Initialize the min-max pair.
    _min, _max = getminmaxpair(array[0], array[1])

    # Triple comparison for every pair of elements
    for ind in xrange(1, len(array)/2):
        pair_min, pair_max = getminmaxpair(array[2 * ind], array[2 * ind + 1])
        _min, fake_min = getminmaxpair(_min, pair_min)
        fake_max, _max = getminmaxpair(_max, pair_max)

    # Adjustment for if len(A) % 2 == 1
    if len(array) % 2 == 1:
        _min, fake_min = getminmaxpair(_min, array[-1])
        fake_max, _max = getminmaxpair(_max, array[-1])

    return _min, _max


def getminmaxpair(a, b):
    if a < b:
        return a, b
    else:
        return b, a
