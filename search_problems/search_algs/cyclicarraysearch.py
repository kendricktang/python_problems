from arraysearch import findfirstoccurrence as ffo


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
        else:
            # array[start] <= array[middle] <= array[end]
            return start
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
                return ffo(array[start:middle], k)
            else:
                # k is not within this sorted half. Check the other half.
                start = middle+1
        else:
            # array[middle:end] is sorted
            if array[middle] < k and k <= array[end]:
                # Do binary search.
                return ffo(array[middle:end+1], k) + middle
            else:
                # k is not within this sorted half. Check the other half.
                end = middle
    return -1
