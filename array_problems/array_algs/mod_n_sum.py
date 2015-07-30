import numpy as np

test = True #

def mod_n_sum(A):
    n=len(A)
    if n:
        mod_n_sum = A[0] % n
        mod_n={}
        mod_n[mod_n_sum] = [0]

        # Bin i into mod_n_sum[[sum mod n of A[0:i]]
        for i in xrange(1,n):
            mod_n_sum = (mod_n_sum + A[i]) % n
            mod_n.setdefault(mod_n_sum,[])
            mod_n[mod_n_sum].append(i)

        # If there is a sum mod n which is zero, that is the answer.
        if mod_n.has_key(0):
            return np.array(xrange(mod_n[0][0]+1))

        # Find i and j in the same bin and subtract to achieve 0 mod n
        for i in xrange(1, len(A)):
            if mod_n.has_key(i) and len(mod_n[i]) > 1:
                return np.array(xrange(mod_n[i][0]+1,mod_n[i][1]+1))
    return A
