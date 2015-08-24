def completionsearch(array, upperbound):
    """Returns s such that sum(min(array[i], s)) = upperbound."""
    array.sort()
    length = len(array)
    prevpsum = 0

    for psum, index in partialsum(array):
        # Find index so that sum(array bound by array[i]) <= upperbound <=
        # sum(array bound by array[i+1])
        approximation = psum + (length - index - 1) * array[index]
        if approximation >= upperbound:
            break
        prevpsum = psum

    index -= 1
    sigma = (upperbound - prevpsum) / float(len(array) - index - 1)
    return sigma


def partialsum(array):
    """A generator for the bounded sum of an array, bounded by array[index] ."""
    psum = 0
    length = len(array)
    for index in xrange(length):
        val = array[index]
        psum += val
        yield psum, index
