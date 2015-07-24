def dutchnationalflag(A, i):
    if i >= len(A):
        raise IndexError("Pivot index is out of bounds")

    swap(A, i, 0)
    pivot = A[0]
    back = 0
    front = 0
    end = len(A)-1

    while front < end:
        if A[front+1] < pivot:
            swap(A, back, front+1)
            back += 1
            front += 1
        elif A[front+1] == pivot:
            front += 1
        else:
            swap(A, front+1, end)
            end -= 1

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]