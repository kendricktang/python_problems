from collections import defaultdict


def mod_n_sum(A):
    """Returns a 2-tuple (a,b) where sum(A[a:b]) == 0 mod n."""
    if not A:
        return A

    # Bin i into mod_n_sum[[sum mod n of A[0:i]]
    mod_n = defaultdict(list, [])
    for mod_n_sum, i in partial_sum_mod_n(A):
        # Early return for sum A[0:i] == 0 mod n
        if mod_n_sum == 0:
            return (0, i + 1)

        # Early return for sum A[0:i] == A[0:j] mod n.
        if mod_n_sum in mod_n:
            return (mod_n[mod_n_sum][0] + 1, i + 1)

        mod_n[mod_n_sum].append(i)


def partial_sum_mod_n(A):
    """Generator which yields the partial sum,
    and the index at which it was summed to
    """
    sum_, i = 0, 0
    n = len(A)
    for x in A:
        sum_ = (sum_ + x) % n
        yield sum_, i
        i += 1
