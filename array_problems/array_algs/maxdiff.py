import numpy as np


def maxdiff(arr):
    """Calculates the max arr[j]-arr[i] where i<j"""
    maximum_diff = 0
    if not arr:
        return maximum_diff

    min_val = arr[0]
    for val in arr:
        min_val = min(val, min_val)
        maximum_diff = max(val-min_val, maximum_diff)

    return maximum_diff


def maxdiff_2(arr):
    """Calculates the max (arr[m]-arr[n])+(arr[j]-arr[i]) where m<n<i<j"""
    maxsumdiff = 0
    if arr:
        diffs_lower = [0]*len(arr)
        min_val = arr[0]
        for i in xrange(len(arr)-1):
            val = arr[i]
            min_val = min(val, min_val)
            maxsumdiff = max(val-min_val, maxsumdiff)
            diffs_lower[i] = maxsumdiff
        max_val = arr[-1]
        for i in xrange(len(arr)-1, -1, -1):
            val = arr[i]
            max_val = max(val, max_val)
            maxsumdiff = max(max_val-val+diffs_lower[i-1], maxsumdiff)

    return maxsumdiff


def maxdiff_k(arr, k):
    """Calculates the maximum sum of k differences"""
    sum_of_k_diffs = np.array([float('-inf')]*(2*k))

    for i in xrange(len(arr)):
        pre_k_sum = sum_of_k_diffs.copy()
        sign = -1
        j = 0
        while j < len(sum_of_k_diffs) and j <= i:
            diff = sign*arr[i]
            if j != 0:
                diff += pre_k_sum[j-1]
            sum_of_k_diffs[j] = max(diff, pre_k_sum[j])
            j += 1
            sign *= -1
    return sum_of_k_diffs[-1]
