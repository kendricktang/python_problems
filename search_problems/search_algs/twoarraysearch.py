def findkthsmallest(array0, array1, k):
    """Finds the kth smallest element between array0 and array1,
    where the two arrays are both sorted with respect to themselves.
    Does it in O(log(k)) time."""
    lower = max(0, k - len(array1))
    upper = min(k, len(array0))
    while lower < upper:
        middle = (upper + lower) / 2

        # Correct potential index out of bound errors.
        array0_correction = _correct_outofbounds(array0, array1, middle - 1)
        array1_correction = _correct_outofbounds(array1, array0, k - middle)

        if array0[middle] < array1[k - middle - 1]:
            # Check array0 for more values and array1 for less values
            lower = middle + 1
        elif array0_correction > array1_correction:
            # check array1 for more values and array1 for less values
            upper = middle - 1
        else:
            # array0[middle-1] <= array1[k-middle] and
            # array0[middle] >= array1[k-middle-1]
            return max(array0_correction, array1[k - middle - 1])

    array0_correction = _correct_outofbounds(array0, array1, lower - 1)
    array1_correction = _correct_outofbounds(array1, array0, k - lower - 1)
    return max(array0_correction, array1_correction)


def _correct_outofbounds(A, B, index):
    # Given A,B sorted arrays and an index,
    # this will return either A[index] if the index is valid,
    # or a value smaller than all elements of B.
    if index < 0 or index >= len(A):
        return B[0] - 1
    else:
        return A[index]
