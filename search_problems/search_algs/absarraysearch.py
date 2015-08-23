def findpairsum(array, k):
    """Given an array sorted by absolute value, find two indices such that
    array[i]+array[j] = k. Return (-1,-1) otherwise."""
    nonnegindices = findnextval(array, lambda array, ind: array[ind] >= 0)
    negindices = findnextval(array, lambda array, ind: array[ind] < 0)
    nonnegindex = nonnegindices.next()
    negindex = negindices.next()
    while nonnegindex >= 0 and negindex >= 0:
        val = array[nonnegindex] + array[negindex]
        if val == k:
            return sorted([nonnegindex, negindex])
        if val > k:
            nonnegindex = nonnegindices.next()
        elif val < k:
            negindex = negindices.next()
        if negindex < 0 or nonnegindex < 0:
            return [-1, -1]


def findnextval(array, func):
    """Finds the next value in an array, beginning from the last index,
    which satisfies the func property."""
    index = len(array) - 1
    while index >= 0:
        if func(array, index):
            yield index
        index -= 1
    yield -1


if __name__ == "__main__":
    array = [-49, 75, 103, -147, 164, -197, -238, 314, 348, -422]
    if not [3, 7] == findpairsum(array, 167):
        print "FAIL"
    elif not [-1, -1] == findpairsum(array, 0):
        print "FAIL"
    else:
        print "PASS"
