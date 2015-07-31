from collections import defaultdict

def mod_n_sum(A):
    """Returns a 2-tuple (a,b) where sum(A[a:b]) == 0 mod n."""
    if not A:
        return A

    # Bin i into mod_n_sum[[sum mod n of A[0:i]]
    n = len(A)
    mod_n = defaultdict(list, [])
    partial_sums = partial_sum_mod_n(A)
    i = 0
    while i < n:
        mod_n_sum = partial_sums.next()

        # Early return for sum A[0:i] == 0 mod n
        if mod_n_sum == 0:
            return (0, i + 1)

        # Early return for sum A[0:i] == A[0:j] mod n.
        if mod_n_sum in mod_n:
            return (mod_n[mod_n_sum][0] + 1, i + 1)

        mod_n[mod_n_sum].append(i)
        i += 1


def partial_sum_mod_n(A):
    n = len(A)
    i = 0
    sum = 0
    while i < n:
        sum = (sum + A[i]) % n
        yield sum
        i += 1
