def findfirstoccurrence(array, k):
    """Given a sorted array, returns the first occurrence of k.
    Returns -1 if it doesn't exist."""
    start = 0
    end = len(array) - 1
    while start < end:
        middle = (start + end)/2
        if array[middle] < k:
            start = middle+1
        else:
            end = middle
    if array[end] == k:
        return end
    return -1


def findfirstelementgreaterthan(array, k):
    """Given a sorted array, returns the first occurrence of an element
    greater than k. Returns -1 if it doesn't exist."""
    start = 0
    end = len(array) - 1
    while start < end:
        middle = (start + end)/2
        if array[middle] <= k:
            start = middle+1
        else:
            end = middle
    if end >= len(array):
        return -1
    return end


def findindexequalsvalue(array):
    """Given a sorted array, find i so that A[i] == i.
    Returns -1 if it doesn't exist."""
    start = 0
    end = len(array) - 1
    while start < end:
        middle = (start + end)/2
        if array[middle] - middle < 0:
            start = middle+1
        elif array[middle] - middle == 0:
            return middle
        else:
            end = middle
    return -1


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


def findstartcyclic(array):
    """Find the smallest index of a cyclically sorted array, assuming all
    elements are distinct."""
    start = 0
    end = len(array) - 1
    while start != end:
        middle = (start + end) / 2
        if array[start] > array[middle]:
            end = middle
        elif array[middle] > array[end]:
            start = middle + 1
    return start


def findincyclic(array, k):
    """Finds the index of k in a cyclically sorted array, assuming all
    elements are distinct."""
    start = 0
    end = len(array) - 1
    while start != end:
        middle = (start + end)/2
        if array[middle] == k:
            # Return for hitting the button on the nose.
            return middle

        if array[start] < array[middle]:
            # This part is sorted
            if array[start] <= k and k < array[middle]:
                # Do binary search.
                return findfirstoccurrence(array[start:middle], k)
            else:
                # k is not within this sorted half. Check the other half.
                start = middle+1
        else:
            # array[middle:end] is sorted
            if array[middle] < k and k <= array[end]:
                # Do binary search.
                return findfirstoccurrence(array[middle:end+1], k) + middle
            else:
                # k is not within this sorted half. Check the other half.
                end = middle
    return -1


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


if __name__ == "__main__":
    array = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    if not array.index(108) == findfirstoccurrence(array, 108):
        print "FAIL"
    if not array.index(285) == findfirstoccurrence(array, 285):
        print "FAIL"
    if not array.index(401) == findfirstoccurrence(array, 401):
        print "FAIL"
    if not 5 == findfirstelementgreaterthan(array, 108):
        print "FAIL"
    if not 2 == findindexequalsvalue(array):
        print "FAIL"

    array = [-49, 75, 103, -147, 164, -197, -238, 314, 348, -422]
    if not [3, 7] == findpairsum(array, 167):
        print "FAIL"
    if not [-1, -1] == findpairsum(array, 0):
        print "FAIL"

    array = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
    if not 4 == findstartcyclic(array):
        print "FAIL"
    if not 0 == findincyclic(array, 378):
        print "FAIL"
    if not 9 == findincyclic(array, 368):
        print "FAIL"

    array = [90, 30, 100, 40, 20]
    if not 60 == completionsearch(array, 210):
        print "FAIL"
