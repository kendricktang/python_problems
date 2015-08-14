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


if __name__ == "__main__":
    array = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    if not array.index(108) == findfirstoccurrence(array, 108):
        print "FAIL"
    elif not array.index(285) == findfirstoccurrence(array, 285):
        print "FAIL"
    elif not array.index(401) == findfirstoccurrence(array, 401):
        print "FAIL"
    elif not 5 == findfirstelementgreaterthan(array, 108):
        print "FAIL"
    elif not 2 == findindexequalsvalue(array):
        print "FAIL"
    else:
        print "PASS"
