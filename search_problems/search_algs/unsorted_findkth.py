def findkthlargest(array, k):
    """Finds the kth largest element in an array."""
    # if there aren't k elements, return None
    if k < 1 or len(array) < k:
        return None
    return _findkthlargest(array, k - 1)


def _findkthlargest(array, k):
    """Recursive helper for findkthlargest()."""
    pivot = getpivot(array)
    firsthalf = [ele for ele in array[0:len(array)] if ele > pivot]
    pivotpart = [ele for ele in array[0:len(array)] if ele == pivot]
    secondhalf = [ele for ele in array[0:len(array)] if ele < pivot]

    if len(firsthalf) > k:
        # Kth element is in the first half:
        return _findkthlargest(firsthalf, k)
    if len(firsthalf) + len(pivotpart) > k:
        # Kth element is the pivot value:
        return pivot
    else:
        # Kth element is in the second half
        return _findkthlargest(secondhalf, k - len(firsthalf) - len(pivotpart))


def getpivot(array):
    """Sorts the first, middle, and last element of array.
    Then moves median to the first element."""
    middle = len(array) / 2
    sorted_three = sorted([array[0], array[middle], array[len(array) - 1]])
    array[0], array[middle], array[len(array) - 1] = sorted_three
    return array[middle]
